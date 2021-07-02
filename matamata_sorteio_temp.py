from ligaroletarussa import RoletaRussa
from random import randint
from openpyxl import load_workbook


roleta = RoletaRussa()
con, cursor = roleta.acessar_banco_de_dados()
cursor.execute("SELECT ID, Nome, Cartoleiro FROM LigaPrincipal ORDER BY Rodada8 DESC;")
todos_times = cursor.fetchall()
lista_times = []
for t in range(64, 96):
    time = todos_times[t]
    time_temp = (time[0], time[1], time[2])
    lista_times.append(time_temp)

numeros_sorteados = []
arquivo = load_workbook('ligaroletarussa2021.xlsx')
planilha = arquivo['MataMataC02']
while True:
    numero = randint(0, 31)
    if numero not in numeros_sorteados:
        numeros_sorteados.append(numero)
    elif len(numeros_sorteados) == 32:
        break

contador_planilha = 1
contador_time = 0
for a  in range(0, 16):
    time = lista_times[numeros_sorteados[a]]
    planilha[f'A{contador_planilha}'] = time[0]
    planilha[f'B{contador_planilha}'] = time[1]
    planilha[f'B{contador_planilha + 2}'] = time[2]
    contador_planilha += 4
contador_planilha = 1
for b in range(16, 32):
    time = lista_times[numeros_sorteados[b]]
    planilha[f'M{contador_planilha}'] = time[0]
    planilha[f'I{contador_planilha}'] = time[1]
    planilha[f'I{contador_planilha + 2}'] = time[2]
    contador_planilha += 4
arquivo.save('ligaroletarussa2021.xlsx')
