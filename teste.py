from ligaroletarussa import Informativos, MataMataDuplas, MataMataLiga, Mensal, PontosLigaEliminatoria, Pontuacao, RoletaRussa, ControleMataMatasLiga
import sqlite3
import requests
import cartolafc


#x = RoletaRussa()
#tabelas = ('LigaEliminatoria', 'LigaPrincipal', 'Mito', 'Patrimonio', 'Returno', 'Turno', 'TimesCadastrados')
#for t in tabelas:
#    x.atualizar_nomes(tabela=t)
#x = MataMataDuplas()
#x.alterar_dupla()

x = RoletaRussa()
con, cursor = x.acessar_banco_de_dados()
cursor.execute('SELECT * FROM MataMataLigaParticipantes WHERE MataMata="A"')
cursor.fetchall()
print(cursor)