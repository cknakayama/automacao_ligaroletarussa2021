from ligaroletarussa import Informativos, MataMataDuplas, MataMataLiga, Mensal, PontosLigaEliminatoria, RoletaRussa
import sqlite3
import requests
import cartolafc

#x = RoletaRussa()
#tabelas = ('LigaEliminatoria', 'LigaPrincipal', 'Mito', 'Patrimonio', 'Returno', 'Turno', 'TimesCadastrados')
#for t in tabelas:
#    x.atualizar_nomes(tabela=t)
x = MataMataDuplas()
x.sorteio()
