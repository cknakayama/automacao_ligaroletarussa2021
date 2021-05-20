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
   
    def pesquisar_time(self, termo_pesquisa=None):
        api = self.acesso_autenticado()
        if not termo_pesquisa:
            termo_pesquisa = str(input('Digite o nome do Time: '))
        times = api.times(query=termo_pesquisa)
        lista_times = []
        for item in times:
            temp = {"id":item.id, "nome":item.nome, "cartoleiro":item.nome_cartola}
            lista_times.append(temp)
        return lista_times

    def pesquisar_liga(self, termo_pesquisa=None):
        api = self.acesso_autenticado()
        if not termo_pesquisa:
            termo_pesquisa = str(input('Digite o nome da Liga: '))
        ligas = api.ligas(query=termo_pesquisa)
        lista_ligas = []
        for item in ligas:
            temp = {"nome":item.nome, "slug":item.slug}
            lista_ligas.append(temp)
        return lista_ligas

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
        
        
    