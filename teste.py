from funcionalidades import *
import sqlite3

x = Funcionalidades()
y = x.pesquisar_time()
x.listar_itens(y)
z = x.escolher_entre_opcoes(y)
w = x.pegar_dados_time_avulso(z)
print(w)