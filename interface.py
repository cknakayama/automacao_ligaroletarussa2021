from os import system
from ligaroletarussa import  (Exibir, CadastroTime, CadastroTimesLiga, 
                            PontosLigaPrincipal, PontosLigaEliminatoria, 
                            Informativos, MataMataLiga, MataMataDuplas)


menu_inicial = [{'opção':'Cadastrar time'},
                {'opção':'Cadastrar times de uma liga'},
                {'opção':'Atualizar informativos'},
                {'opção':'Criar Mata-matas da Liga'},
                {'opção':'Atualizar Pontos Mata-matas da Liga - COM CAPITÃO'},
                {'opção':'Atualizar Pontos Mata-matas da Liga - SEM CAPITÃO'},
                {'opção':'Criar Mata-mata em Duplas'},
                {'opção':'Atualizar Pontos Mata-mata Duplas - COM CAPITÃO'},
                {'opção':'Atualizar Pontos Mata-mata Duplas - SEM CAPITÃO'}]

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
            elif escolha['opção']  == 'Cadastrar times de uma liga':
                self.escolha_cadastrar_times_liga()
            elif escolha['opção']  == 'Atualizar informativos':
                self.escolha_atualizar_informativos()
            elif escolha['opção'] == 'Criar Mata-matas da Liga':
                self.escolha_criar_mata_mata_liga()
            elif escolha['opção'] == 'Atualizar Pontos Mata-matas da Liga - COM CAPITÃO':
                self.escolha_pontos_mata_mata_liga_com_capitao()
            elif escolha['opção'] == 'Atualizar Pontos Mata-matas da Liga - SEM CAPITÃO':
                self.escolha_pontos_mata_mata_liga_sem_capitao()
            elif escolha['opção'] == 'Criar Mata-mata em Duplas':
                self.escolha_criar_mata_mata_duplas()
            elif escolha['opção'] == 'Atualizar Pontos Mata-mata Duplas - COM CAPITÃO':
                self.escolha_pontos_mata_mata_duplas_com_capitao()
            elif escolha['opção'] == 'Atualizar Pontos Mata-mata Duplas - SEM CAPITÃO':
                self.escolha_pontos_mata_mata_duplas_sem_capitao()
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
                return escolha

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
            elif escolha['opção'] == 'Voltar ao Menu Principal':
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
            elif escolha['opção'] == 'Voltar ao Menu Principal':
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
    
    def escolha_criar_mata_mata_liga(self):
        """
        Método que chama as classes para criar os Mata-matas
        Série A, B e C da Liga Principal em uma planilha do Excel.
        """
        self.exibir_cabecalho('Criando Mata-matas da Liga')
        while True:
            escolha = str(input('As Ligas criadas anteriormente serão apagadas, deseja continuar? [S/N] ')).upper().strip()
            if escolha == 'S':
                mm = MataMataLiga()
                mm.criar_mata_matas()
                break
            elif escolha == 'N':
                break
            else:
                print('Opção inválida. Teste novamente.')

    def escolha_pontos_mata_mata_liga_com_capitao(self):
        """
        Método que chama as classes para atualizar os pontos dos Mata-matas
        Série A, B e C da Liga Principal em uma planilha do Excel.
        """
        self.exibir_cabecalho('Atualizando Pontos dos Mata-matas da Liga')
        mm = MataMataLiga()
        mm.pontuacao_com_capitao()

    def escolha_pontos_mata_mata_liga_sem_capitao(self):
        """
        Método que chama as classes para atualizar os pontos dos Mata-matas
        Série A, B e C da Liga Principal em uma planilha do Excel.
        """
        self.exibir_cabecalho('Atualizando Pontos dos Mata-matas da Liga')
        mm = MataMataLiga()
        mm.pontuacao_sem_capitao()
        
    def escolha_criar_mata_mata_duplas(self):
        """
        Método que chama as classes para criar os Mata-matas
        em Duplas em uma planilha do Excel.
        """
        self.exibir_cabecalho('Criando Mata-mata em Duplas')
        while True:
            escolha = str(input('A Liga criada anteriormente será apagada, deseja continuar? [S/N] ')).upper().strip()
            if escolha == 'S':
                mmd = MataMataDuplas()
                mmd.criar_mata_mata_duplas()
                break
            elif escolha == 'N':
                break
            else:
                print('Opção inválida. Teste novamente.')
    
    def escolha_pontos_mata_mata_duplas_com_capitao(self):
        """
        Método que chama as classes para atualizar os pontos dos Mata-matas
        em Duplas em uma planilha do Excel.
        """
        self.exibir_cabecalho('Atualizando Pontos dos Mata-mata em Duplas')
        mmd = MataMataDuplas()
        mmd.pontuacao_com_capitao()
    
    def escolha_pontos_mata_mata_duplas_sem_capitao(self):
        """
        Método que chama as classes para atualizar os pontos dos Mata-matas
        em Duplas em uma planilha do Excel.
        """
        self.exibir_cabecalho('Atualizando Pontos dos Mata-mata em Duplas')
        mmd = MataMataDuplas()
        mmd.pontuacao_sem_capitao()
    