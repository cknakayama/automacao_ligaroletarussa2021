from ligaroletarussa import *


class MataMatasLiga(Pontuacao):
    def __init__(self):
        super().__init__()
    
    def cadastrar_times(self):
        api = self.acesso_autenticado()
        con, cursor = self.acessar_banco_de_dados()
        liga = api.liga(slug="roleta-ru-a", order_bt="rodada").times
        contador = 0
        for time in liga:
            if contador < 32:
                mata_mata = "A"
            elif 32 <= contador < 64:
                mata_mata = "B"
            elif 64 <= contador < 96:
                mata_mata = "C"
            else:
                break
            time = liga[contador]
            dados = (mata_mata, time["id"], time["nome"], time["nome_cartola"])
            cursor.execute(f'INSERT INTO MataMataLigaParticipantes(MataMata, ID, Nome_Time, Nome_Cartoleiro) VALUES{dados}')
            con.commit()


