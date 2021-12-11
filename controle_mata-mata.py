from ligaroletarussa import *


class MataMatasLiga(Pontuacao):
    tabelas = ("MataMataA", "MataMataB", "MataMataC")

    def atualizar_pontuacao(self):
        api = self.acesso_autenticado()
        arquivo = load_workbook('Planilha-Mata-matas.xlsx')
        for tabela in tabelas:
            planilha = arquivo(tabela)
            contador = 2
            while True:
                id = planilha[f'C{contador}']
                time = api.time(id=id, as_json=True)
            


