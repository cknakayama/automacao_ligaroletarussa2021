from ligaroletarussa import Informativos, MataMataDuplas, MataMataLiga, Mensal, PontosLigaEliminatoria, Pontuacao, RoletaRussa
import sqlite3
import requests
import cartolafc


#x = RoletaRussa()
#tabelas = ('LigaEliminatoria', 'LigaPrincipal', 'Mito', 'Patrimonio', 'Returno', 'Turno', 'TimesCadastrados')
#for t in tabelas:
#    x.atualizar_nomes(tabela=t)
#x = MataMataDuplas()
#x.alterar_dupla()

x = Pontuacao()
api = x.acesso_autenticado()
liga = api.liga(slug="roleta-ru-a", order_by="rodada").times
for time in liga:
    print(time)