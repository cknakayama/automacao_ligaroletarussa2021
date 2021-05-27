from ligaroletarussa import *
import os

menu_inicial = [{'opção':'Cadastrar times'},
                {'opção':'Cadastrar times de uma liga'},
                {'opção':'Atualizar informativos'},
                {'opção':'Criar Liga Mata-mata'},
                {'opcao':'Criar Liga Mata-mata em Duplas'}]

opcoes_de_ligas = [{'opção':'Liga Principal'},
                   {'opção':'Liga Eliminatória'}]

class Interface(Exibir):
    
    def menu_principal(self):
        """
        Método que exibe o menu principal no terminal.
        O usuário pode escolher entre as opções ou sair do programa.
        
        Retorna:    escolha - retorna uma string com a escolha do usuário.
        """
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

    def escolha_cadastrar_times(self):
        opcoes= [{'opção':'Continuar Cadastrando'},
                {'opção':'Voltar ao Menu Principal'}]
        while True:
            self.exibir_cabecalho('Cadastrar Time')
            CadastroTime()
            self.listar_itens(opcoes)
            escolha = self.escolher_entre_opcoes(opcoes)
            if not escolha:
                os.system('cls') or None
                print('Saindo do Programa')
                exit()
            elif escolha == 'Voltar ao Menu Principal':
                self.menu_principal()

            
