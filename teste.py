from funcionalidades import *
import sqlite3
import requests
import cartolafc


x = Funcionalidades()
#y = x.pesquisar_liga()
#x.listar_itens(y)
#z = x.escolher_entre_opcoes(y)
#w = x.pegar_pontuacao_times_liga(z)
#print(w)

y = x.pesquisar_time()
x.listar_itens(y)
z = x.escolher_entre_opcoes(y)
x.cadastrar_time_BD(tabela='LigaPrincipal', dados=z)
