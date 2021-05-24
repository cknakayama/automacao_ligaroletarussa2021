import cartolafc
import sqlite3
import os
import requests


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

class Tela:
    @staticmethod
    def exibir_cabecalho(texto=''):
        os.system('cls') or None
        print('-'*39)
        print(f"|{texto.upper():^37}|")
        print('-'*39)

    @staticmethod
    def listar_itens(lista):
        chaves = [key for key in lista[0].keys()]
        maiores = []
        for chave in chaves:
            valor_maior = 0
            for item in lista:
                if len(str(item[chave])) > valor_maior:
                    valor_maior = len(str(item[chave]))
                else:
                    pass
            maiores.append(valor_maior)
        print(f" {'No':_^4} ", end="")
        for c in range(0, len(chaves)):
            print(f" {chaves[c].upper():_^{maiores[c]+2}} ", end="")
        print()
        numero = 1
        for dic in lista:
            print(f" {(numero):^4} ", end="")
            for c in range(0, len(chaves)):
                print(f" {dic[chaves[c]]:<{maiores[c]+2}} ", end="")
            print()
            numero += 1
        print(f" {'0':^4}  Nenhuma das alternativas")
   
    @staticmethod
    def int_input(texto=''):
        while True:
            try:
                entrada = int(input(texto))
            except ValueError:
                print('Digite um valor válido.')
            else:
                break
        return entrada

    def escolher_entre_opcoes(self, dicionario):
        while True:
            escolha = self.int_input(f'Escolha uma das opções entre 1 e {len(dicionario)} e digite aqui sua escolha: ')
            if escolha == 0:
                return False
            elif 0 < escolha <= len(dicionario):
                return dicionario[escolha-1]
            else:
                print('Opção inválida.')
    
    def escolher_ligas_roleta_russa(self):
        self.listar_itens(opcoes_de_ligas)
        escolha = self.escolher_entre_opcoes(opcoes_de_ligas)
        return escolha['tabela']

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
            except:
                print(f'Já existe um cadastro do time {dados_time[1]}.')
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
                t = {'pontos':None}
            pontuacoes.append({'id':id[0], 'pontos':t['pontos']})
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
        cursor.execute(f"UPDATE {tabela} SET {coluna}={pontos['pontos']} WHERE ID={pontos['id']}")
        con.commit()
    
class PontosLigaPrincipal(Pontuacao):
    def __init__(self):
        super().__init__()
        tabela = 'LigaPrincipal'
        coluna = f"Rodada{self.rodada_atual}"
        pontos = self.pegar_pontuacao_dos_times(tabela='LigaPrincipal')
        for p in pontos:
            self.salvar_pontos(tabela=tabela, coluna = coluna, pontos = p)
        print('Pontuação dos times da Liga Principal salvas com SUCESSO.')

class PontosLigaEliminatoria(Pontuacao):
    def __init__(self):
        super().__init__()
        tabela = 'LigaEliminatoria'
        pontos = self.pegar_pontuacao_dos_times(tabela='LigaEliminatoria')
        for p in pontos:
            self.salvar_pontos(tabela=tabela, coluna = 'PtsRodada', pontos = p)
        print('Pontuação dos times da Liga Principal salvas com SUCESSO.')

class Patrimonio(Pontuacao):
    pass

class Mito(Pontuacao):
    pass

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


