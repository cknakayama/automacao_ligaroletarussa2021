from os import system
from ligaroletarussa import  (Exibir, CadastroTime, CadastroTimesLiga, 
                            PontosLigaPrincipal, PontosLigaEliminatoria, 
                            Informativos)


menu_inicial = [{'opção':'Cadastrar time'},
                {'opção':'Cadastrar times de uma liga'},
                {'opção':'Atualizar informativos'},
                {'opção':'Criar Liga Mata-mata'},
                {'opção':'Criar Liga Mata-mata em Duplas'}]

opcoes_de_ligas = [{'opção':'Liga Principal'},
                   {'opção':'Liga Eliminatória'}]


class Interface(Exibir):
    def __init__(self) -> None:
        super().__init__()
        while True:
            escolha = self.menu_principal()
            if not escolha:
                system('cls') or None
                print('Saindo do Programa')
                exit()
            elif escolha['opção'] == 'Cadastrar time':
                self.escolha_cadastrar_time()
            elif escolha['opção'] == 'Cadastrar times de uma liga':
                self.escolha_cadastrar_times_liga()
            elif escolha['opção'] == 'Atualizar informativos':
                self.escolha_atualizar_informativos()
            else:
                print('Opção ainda não foi implementada.')
        
    
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
                return {}
            else:
                return escolha['opção']

    def escolha_cadastrar_time(self):
        """
        Método que chama a classe para cadastrar times avulsos.
        """
        opcoes= [{'opção':'Continuar Cadastrando'},
                {'opção':'Voltar ao Menu Principal'}]
        while True:
            self.exibir_cabecalho('Cadastrar Time')
            CadastroTime()
            self.listar_itens(opcoes)
            escolha = self.escolher_entre_opcoes(opcoes)
            if not escolha:
                system('cls') or None
                print('Saindo do Programa')
                exit()
            elif escolha == 'Voltar ao Menu Principal':
                break

    def escolha_cadastrar_times_liga(self):
        """
        Método que chama a classe para cadastrar times de uma liga.
        """
        opcoes= [{'opção':'Continuar Cadastrando'},
                {'opção':'Voltar ao Menu Principal'}]
        while True:
            self.exibir_cabecalho('Cadastrar Times da Liga')
            CadastroTimesLiga()
            self.listar_itens(opcoes)
            escolha = self.escolher_entre_opcoes(opcoes)
            if not escolha:
                system('cls') or None
                print('Saindo do Programa')
                exit()
            elif escolha == 'Voltar ao Menu Principal':
                break
            
    def escolha_atualizar_informativos(self):
        """
        Método que chama as classes para atualizar as pontuações e 
        os informativos.
        """
        self.exibir_cabecalho('Atualizando Informativos')
        PontosLigaPrincipal()
        PontosLigaEliminatoria()
        Informativos()