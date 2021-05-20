from funcionalidades import *
import os

os.system('cls') or None

menu_inicial = [{'opção':'Cadastrar times de uma liga'},
                {'opção':'Cadastrar times avulso'},
                {'opção':'Atualizar pontuações de ligas'},
                {'opção':'Criar Liga Mata-mata'}]

func = Funcionalidades()
while True:
    print('-'*39)
    print(f"|{'MENU PRINCIPAL':^37}|")
    print('-'*39)
    func.listar_itens(menu_inicial)
    escolha = func.escolher_entre_opcoes(menu_inicial)
    if not escolha:
        os.system('cls') or None
        pass
    else:
        break
os.system('cls') or None
print('-'*39)
print(f"|{escolha['opção'].upper():^37}|")
print('-'*39)