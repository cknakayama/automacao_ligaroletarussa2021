from sqlite3.dbapi2 import IntegrityError, OperationalError
import cartolafc
import sqlite3
import requests
from interface import Tela


opcoes_de_ligas = [{'opção':'Liga Principal', 'tabela':'LigaPrincipal'},
                   {'opção':'Liga Eliminatória', 'tabela':'LigaEliminatoria'}]

class RoletaRussa:
    def __init__(self):
        self.banco_de_dados = "ligaroletarussa2021.db"

    def acessar_banco_de_dados(self):
        con = sqlite3.connect(self.banco_de_dados)
        cursor = con.cursor()
        return con, cursor

    def pegar_autenticacao(self):
        con, cursor = self.acessar_banco_de_dados()
        cursor.execute("SELECT cookie FROM Auth")
        auth = cursor.fetchall()
        return auth[0][0]
    
    def trocar_autenticacao(self):
        nova_autenticacao = str(input('Digite a nova autenticação: '))
        con, cursor = self.acessar_banco_de_dados()
        cursor.execute(f'UPDATE Auth SET cookie={nova_autenticacao}')
        con.commit()
    
    def acesso_autenticado(self):
        api = cartolafc.Api()
        while True:
            try:
                api._glb_id = self.pegar_autenticacao()
                api.ligas(query='')
            except:
                print("Erro de login.")
                self.trocar_autenticacao()
            else:
                break
        return api

class CadastroTime(RoletaRussa):
    def __init__(self, dados=None, tabela=None):
        super().__init__()
        tela = Tela()
        if dados:
            time = dados
        else:   
            lista_times = self.pesquisar_time()
            tela.listar_itens(lista_times)
            time = tela.escolher_entre_opcoes(lista_times)
        if tabela:
            tabela=tabela
        else:
            tabela = tela.escolher_ligas_roleta_russa()
        self.cadastrar_time_no_BD(tabela=tabela, dados=time)
    
    def pesquisar_time(self, termo_pesquisa=None):
        lista_times = []
        api = self.acesso_autenticado()
        if not termo_pesquisa:
            termo_pesquisa = str(input('Digite o nome do Time: ')).strip()
        times = api.times(query=termo_pesquisa)
        for item in times:
            temp = {"id":item.id, "nome":item.nome, "cartoleiro":item.nome_cartola}
            lista_times.append(temp)
        return lista_times

    def cadastrar_time_no_BD(self, tabela, dados):
            dados_time = (dados['id'], dados['nome'], dados['cartoleiro'])
            con, cursor = self.acessar_banco_de_dados()
            try:
                cursor.execute(f'INSERT INTO {tabela}(ID, Nome, Cartoleiro) VALUES{dados_time}')
            except IntegrityError:
                print(f'Já existe um cadastro do time {dados_time[1]}.')
                pass
            except OperationalError:
                print(f'Não existe a tabela {tabela}.')
                pass
            else:
                con.commit()
            dados_time2 = (dados['id'], dados['nome'], dados['cartoleiro'], 'OK')
            try:
                cursor.execute(f'INSERT INTO TimesCadastrados(ID, Nome, Cartoleiro, {tabela}) VALUES{dados_time2}')
            except IntegrityError:
                cursor.execute(f'UPDATE TimesCadastrados SET {tabela}="OK" WHERE ID={dados_time2[0]}')
                con.commit()
            except OperationalError:
                print(f'Não existe a coluna {tabela}.')
                pass
            else:
                con.commit()
            print(f'Time {dados_time[1]} foi cadastrado com sucesso.')

class CadastroTimesLiga(RoletaRussa):
    def __init__(self):
        super().__init__()
        lista_ligas = self.pesquisar_liga()
        tela = Tela()
        tela.listar_itens(lista_ligas)
        liga = tela.escolher_entre_opcoes(lista_ligas)
        tabela = tela.escolher_ligas_roleta_russa()
        self.cadastrar_times_de_liga_BD(liga=liga, tabela=tabela)
        if tabela == 'LigaPrincipal':
            self.cadastrar_times_de_liga_BD(liga=liga, tabela='Patrimonio')
            self.cadastrar_times_de_liga_BD(liga=liga, tabela='Turno')
            self.cadastrar_times_de_liga_BD(liga=liga, tabela='Returno')


    def pesquisar_liga(self, termo_pesquisa=None):
        lista_ligas = []
        api = self.acesso_autenticado()
        if not termo_pesquisa:
            termo_pesquisa = str(input('Digite o nome da Liga: ')).strip()
        ligas = api.ligas(query=termo_pesquisa)
        for item in ligas:
            temp = {"nome":item.nome, "slug":item.slug}
            lista_ligas.append(temp)
        return lista_ligas
    
    def pegar_times_liga(self, liga):
        api = self.acesso_autenticado()
        liga_slug = str(liga['slug'])
        times_liga = api.liga(slug=liga_slug)
        return times_liga.times

    def cadastrar_times_de_liga_BD(self, liga, tabela):
        times = self.pegar_times_liga(liga)
        for time in times:
            t = {'id':time.id, 'nome':time.nome, 'cartoleiro':time.nome_cartola}
            CadastroTime(dados=t, tabela=tabela)
        print('Times da liga foram salvos.')

class Pontuacao(RoletaRussa):
    def __init__(self):
        super().__init__()
        self.rodada_atual = self.rodada() - 1

    def pegar_pontuacao_dos_times(self, tabela):
        con, cursor = self.acessar_banco_de_dados()
        cursor.execute(f'select ID from {tabela}')
        lista_id = cursor.fetchall()
        api = self.acesso_autenticado()
        pontuacoes = []
        for id in lista_id:
            try:
                t = api.time(id=id[0], as_json=True)
            except:
                t = {'pontos':None, 'patrimonio':None}
            pontuacoes.append({'id':id[0], 'pontos':t['pontos'], 'patrimonio':t['patrimonio']})
        return pontuacoes

    def rodada(self):
        try:
            url_1 = 'https://api.cartolafc.globo.com/mercado/status'
            r = requests.get(url=url_1)
            status = r.json()
        except:
            print('Não foi possível pegar a rodada no sistema.')
            tela = Tela()
            return tela.int_input('Digite a rodada:')
        else:
            return status['rodada_atual']

    def salvar_pontos(self, tabela, coluna, pontos):
        con, cursor = self.acessar_banco_de_dados()
        try:
            cursor.execute(f"UPDATE {tabela} SET {coluna}={pontos['pontos']} WHERE ID={pontos['id']}")
        except:
            print(f'Coluna {coluna} não existe.')
            pass
        else:
            con.commit()
    
class PontosLigaPrincipal(Pontuacao):
    def __init__(self):
        super().__init__()
        coluna = f'Rodada{self.rodada_atual}'
        pontos = self.pegar_pontuacao_dos_times(tabela='LigaPrincipal')
        self.salvar_principal(coluna=coluna, pontos=pontos)
        self.salvar_mito()
        print('Pontuação dos times da Liga Principal salvas com SUCESSO.')
    
    def salvar_principal(self, coluna, pontos):
        for p in pontos:
            self.salvar_pontos(tabela='LigaPrincipal', coluna=coluna, pontos=p)
            self.salvar_patrimonio(pontos=p)
            self.salvar_turno_returno(coluna=coluna, pontos=p)
            self.salvar_pontos_total('LigaPrincipal')
            self.salvar_pontos_total('Turno')
            self.salvar_pontos_total('Returno')

    def salvar_patrimonio(self, pontos):
        con, cursor = self.acessar_banco_de_dados()
        cursor.execute(f"UPDATE Patrimonio SET C$={pontos['patrimonio']} WHERE ID={pontos['id']}")
        con.commit()

    def salvar_mito(self):
        con, cursor = self.acessar_banco_de_dados()
        cursor.execute(f"SELECT ID, Nome, Cartoleiro, Rodada{self.rodada_atual} FROM LigaPrincipal ORDER BY Rodada{self.rodada_atual} LIMIT 3")
        times = cursor.fetchall()
        for t in times:
            valores = (t[0], t[1], t[2], self.rodada_atual, t[3])
            cursor.execute(f"INSERT INTO Mito(ID, Nome, Cartolero, Rodada, Pontuacao) VALUES{valores}")
            con.commit()
        
    def salvar_turno_returno(self, coluna, pontos):
        if self.rodada_atual <= 19:
            self.salvar_pontos(tabela='Turno', coluna=coluna, pontos=pontos)
        else:
            self.salvar_pontos(tabela='Returno', coluna=coluna, pontos=pontos)
            
    def salvar_pontos_total(self, tabela):
        con, cursor = self.acessar_banco_de_dados()
        cursor.execute(f"SELECT ID FROM {tabela}")
        id = cursor.fetchall()
        cursor.execute(f"PRAGMA table_info({tabela})")
        col = cursor.fetchall()
        for t in id:
            pontos_total = 0
            for coluna in col[4:]:
                cursor.execute(f"SELECT {coluna[1]} FROM {tabela} WHERE ID={t[0]}")
                if cursor.fetchall()[0][0]:
                    pontos_total += cursor.fetchall()[0][0]
                else:
                    pass
            cursor.execute(f"UPDATE {tabela} SET PtsTotal={pontos_total} WHERE ID={t[0]}")
            con.commit()

class PontosLigaEliminatoria(Pontuacao):
    def __init__(self):
        super().__init__()
        tabela = 'LigaEliminatoria'
        pontos = self.pegar_pontuacao_dos_times(tabela='LigaEliminatoria')
        for p in pontos:
            self.salvar_pontos(tabela=tabela, coluna = 'PtsRodada', pontos = p)
        print('Pontuação dos times da Liga Principal salvas com SUCESSO.')

class Turno(Pontuacao):
    pass

class Returno(Pontuacao):
    pass

class Informativo(Pontuacao):
    def __init__(self):
        super().__init__()
        self.con, self.cursor = self.acessar_banco_de_dados()

    def top_10(self):
        coluna = f"Rodada{self.rodada_atual}"
        self.cursor.execute("SELECT nome, {coluna} FROM LigaPrincipal order by {coluna} limit 10")
        top10 = self.cursor.fetchall()


