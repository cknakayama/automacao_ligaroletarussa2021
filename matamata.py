from ligaroletarussa import Exibir, Pontuacao
from os import system


class MataMata(Pontuacao):
    def __init__(self):
        super().__init__()
        self.tela = Exibir()

    def escolher_mata_mata(self):
        opcoes = [{'opção':'Mata-mata Liga Principal'}, 
                  {'opção':'Mata-mata Avulso'}, 
                  {'opção':'Mata-mata em Duplas'}]
        self.tela.listar_itens(opcoes)
        escolha = self.tela.escolher_entre_opcoes(opcoes)
        if not escolha:
            system('cls') or None
            print('Saindo do Programa')
            exit()
        elif escolha['opção'] == 'Mata-mata Liga Principal':
            self.mm_liga_principal()
        elif escolha['opção'] == 'Mata-mata Avulso':
            self.mm_avulso()
        else:
            self.mm_duplas()

    def mm_liga_principal(self):
        opcoes = [{}]

    def mm_avulso(self):
        pass

    def mm_duplas(self):
        pass

    