from ligaroletarussa import *
import os

menu_inicial = [{'opção':'Cadastrar times de uma liga'},
                {'opção':'Cadastrar times avulso'},
                {'opção':'Atualizar pontuações de ligas'},
                {'opção':'Criar Liga Mata-mata'}]

opcoes_de_ligas = [{'opção':'Liga Principal', 'tabela':'LigaPrincipal'},
                   {'opção':'Liga Eliminatória', 'tabela':'LigaEliminatoria'}]



def menu_principal(self):
    while True:
        self.exibir_cabecalho('Menu Principal')
        self.listar_itens(menu_inicial)
        escolha = self.escolher_entre_opcoes(menu_inicial)
        if not escolha:
            os.system('cls') or None
            print('Saindo do Programa')
            exit()
        else:
            return escolha['opção']
