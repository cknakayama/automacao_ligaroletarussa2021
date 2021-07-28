from ligaroletarussa import Pontuacao
from openpyxl import load_workbook


roleta = Pontuacao()
api = roleta.acesso_autenticado()
arquivo = load_workbook('ligaroletarussa2021.xlsx')
planilha = arquivo['MataMataC02']
contador = 1
while True:
    id = planilha[f'A{contador}'].value
    if id:
        time = api.time(id=id, as_json=True)
        pontos = 0
        for jogador in time['atletas']:
            pontos += jogador['pontos_num']
        planilha[f'F{contador}'] = pontos
        contador += 4
    else:
        break
contador = 1
while True:
    id = planilha[f'M{contador}'].value
    if id:
        time = api.time(id=id, as_json=True)
        pontos = 0
        for jogador in time['atletas']:
            pontos += jogador['pontos_num']
        planilha[f'H{contador}'] = pontos
        contador += 4
    else:
        break
arquivo.save('ligaroletarussa2021.xlsx')