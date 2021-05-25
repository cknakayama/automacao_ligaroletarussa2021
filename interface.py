from ligaroletarussa import *
import os

menu_inicial = [{'opção':'Cadastrar times de uma liga'},
                {'opção':'Cadastrar times avulso'},
                {'opção':'Atualizar pontuações de ligas'},
                {'opção':'Criar Liga Mata-mata'}]

opcoes_de_ligas = [{'opção':'Liga Principal', 'tabela':'LigaPrincipal'},
                   {'opção':'Liga Eliminatória', 'tabela':'LigaEliminatoria'}]

class Tela:
    @staticmethod
    def exibir_cabecalho(texto=''):
        os.system('cls') or None
        print('-'*39)
        print(f"|{texto.upper():^37}|")
        print('-'*39)

    @staticmethod
    def listar_itens(lista):
        chaves = [key for key in lista[0].keys()]
        maiores = []
        for chave in chaves:
            valor_maior = 0
            for item in lista:
                if len(str(item[chave])) > valor_maior:
                    valor_maior = len(str(item[chave]))
                else:
                    pass
            maiores.append(valor_maior)
        print(f" {'No':_^4} ", end="")
        for c in range(0, len(chaves)):
            print(f" {chaves[c].upper():_^{maiores[c]+2}} ", end="")
        print()
        numero = 1
        for dic in lista:
            print(f" {(numero):^4} ", end="")
            for c in range(0, len(chaves)):
                print(f" {dic[chaves[c]]:<{maiores[c]+2}} ", end="")
            print()
            numero += 1
        print(f" {'0':^4}  Nenhuma das alternativas")
   
    @staticmethod
    def int_input(texto=''):
        while True:
            try:
                entrada = int(input(texto))
            except ValueError:
                print('Digite um valor válido.')
            else:
                break
        return entrada

    def escolher_entre_opcoes(self, dicionario):
        while True:
            escolha = self.int_input(f'Escolha uma das opções entre 1 e {len(dicionario)} e digite aqui sua escolha: ')
            if escolha == 0:
                return False
            elif 0 < escolha <= len(dicionario):
                return dicionario[escolha-1]
            else:
                print('Opção inválida.')
    
    def escolher_ligas_roleta_russa(self):
        self.listar_itens(opcoes_de_ligas)
        escolha = self.escolher_entre_opcoes(opcoes_de_ligas)
        return escolha['tabela']

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
