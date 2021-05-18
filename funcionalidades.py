import cartolafc
import sqlite3


class Funcionalidades:
    def __init__(self):
        self.banco_de_dados = "ligaroletarussa2021.db"

    def acessar_banco_de_dados(self):
        return sqlite3.connect(self.banco_de_dados)

    def pegar_autenticacao(self):
        con = self.acessar_banco_de_dados()
        cursor = con.cursor()
        cursor.execute("SELECT cookie FROM Auth;")
        auth = cursor.fetchall()
        return auth[0][0]
    
    def acesso_autenticado(self):
        api = cartolafc.Api()
        api._glb_id = self.pegar_autenticacao()
        return api
    
    


        
    