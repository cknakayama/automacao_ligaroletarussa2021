import cartolafc
import sqlite3


class Funcionalidades:
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

    def listar_itens(self, dicionario):
        c = 1
        for item in dicionario:
            print(f"{c}: ", end=" ")
            for k,i in item.items():
                print(f"{k} - {i}", end=" ")
            print()
            print("-="*20)
            c += 1
        
    def pesquisar_time(self, termo_pesquisa):
        api = self.acesso_autenticado()
        times = api.times(query=str(termo_pesquisa))
        lista_times = []
        for item in times:
            temp = {"id":item.id, "nome":item.nome, "cartoleiro":item.nome_cartola}
            lista_times.append(temp)
        return lista_times

    def pesquisar_liga(self, termo_pesquisa):
        api = self.acesso_autenticado()
        ligas = api.ligas(query=str(termo_pesquisa))
        lista_ligas = []
        for item in ligas:
            temp = {"nome":item.nome, "slug":item.slug}
            lista_ligas.append(temp)
        return lista_ligas



        
    