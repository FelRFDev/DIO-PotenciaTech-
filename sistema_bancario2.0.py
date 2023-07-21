"""
Desafio parte 2 - Refatorando o código!

- Separar as funções existentes de saque depósito e extrato em Funções! Cada função deverá ter uma regra
na passagem de argumentos.

* A função de saque deve receber argumentos somente por **Kwargs.
* A função de depósito deve receber os argumentos somente por posição.
* A função de extrato deve receber os argumentos de forma posicional e **kwargs (Argumento posicional: saldo / Argumento Nomeado: Extrato)

- Criar duas novas funções: Cadastrar usuário (Cliente) e cadastrar conta bancária!

* Criar Usuário: O programa deve armazenar os usuários em uma Lista. Um usuário é composto por
(Nome, Data de nascimento, Cpf e Endereço). O endereço é uma string com o formato de: 
Logradouro / número / bairro / cidade-sigla do estado. Deve ser armazenado somente os 
números do cpf (sem o - ). Não podemos cadastrar mais de um usuário com o mesmo cpf. 
Utilizar dicionários

* Criar Conta Corrente: O programa deve armazenar contas em uma lista. Uma conta é composta por:
(Agência, Número da conta e Usuário). O número da conta é sequencial, iniciando em 1. O número da
agência é fixo (0001). O usuário pode ter mais de uma conta, mas a conta pertence somente a um usuário.

DICA:
Ao criar um usuário, o mesmo não terá uma conta vinculada portanto, para criar esse vínculo, filtre a lista de usuários
de acordo com o cpf informado para cada usuário da lista. Caso encontre, basta vincular a conta ao usuário encontrado.

"""

from datetime import datetime
from tabulate import tabulate


sistem_logo="""███████╗██╗███████╗████████╗███████╗███╗   ███╗ █████╗                            
██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔══██╗                           
███████╗██║███████╗   ██║   █████╗  ██╔████╔██║███████║                           
╚════██║██║╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║                           
███████║██║███████║   ██║   ███████╗██║ ╚═╝ ██║██║  ██║                           
╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝                           
                                                                                  
██████╗  █████╗ ███╗   ██╗ ██████╗ █████╗ ██████╗ ██╗ ██████╗      ██╗    ██████╗ 
██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔══██╗██╔══██╗██║██╔═══██╗    ███║   ██╔═████╗
██████╔╝███████║██╔██╗ ██║██║     ███████║██████╔╝██║██║   ██║    ╚██║   ██║██╔██║
██╔══██╗██╔══██║██║╚██╗██║██║     ██╔══██║██╔══██╗██║██║   ██║     ██║   ████╔╝██║
██████╔╝██║  ██║██║ ╚████║╚██████╗██║  ██║██║  ██║██║╚██████╔╝     ██║██╗╚██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝      ╚═╝╚═╝ ╚═════╝"""



colorir = {
    "Vermelho":'\033[31m',
    'Verde':'\033[32m',
    'Fecha_Cor':'\033[m',
    "Laranja": '\033[34m'
}

class Operacoes:
    """_ Classe resposnável por conter as principais funcionalidades do sistema principal. _
    """

    def sacar(self, valor: float = 0, saldo: float = 0, qtd_saque: int = 0, hora: str = '') -> None:
    
        """_ Método responsável por realizar a operação de saque após fazer algumas validações
        na conta bancária do usuário. _

        Args:
            valor (float): _ Representa o valor a ser sacado informado pelo usuário. _
            saldo (float): _ Representa o saldo atual da conta bancária do usuário. _
            qtd_saque (int): _ Representa quantas vezes o usuário já realizou a operação de saque no dia. _
            hora (str): _ Representa o horário no qual foi realizada a operação. _
        """
        match saldo:
            case 0:
                print(f'\n{colorir["Vermelho"]}Você não possui saldo suficiente para sacar!{colorir["Fecha_Cor"]}')

            case _ :
                match valor:
                    case _ as positivo if positivo == 0 or positivo < 0:
                        print(f'\n{colorir["Vermelho"]}Só é permitido valores positivos!{colorir["Fecha_Cor"]}')
                    
                    case _ as quantidade if quantidade > 500:
                        print(f'\n{colorir["Vermelho"]}Só é permitido sacar valores até R$500,00. Tente novamente!{colorir["Fecha_Cor"]}')

                    case _ as quantidade if quantidade > 0 and quantidade <= 500 and saldo > 0 and qtd_saque < 3:
                        self.saldo -= valor
                        self.dados_extrato["Quantidade de Saques"][0] += 1
                        self.dados_extrato["Informações dos Saques"]["Valores"].append(valor)
                        self.dados_extrato["Informações dos Saques"]["Horários"].append(hora)
                        print(f'\n{colorir["Laranja"]}O valor de R$ {valor:.2f} foi sacado com sucesso! Saldo atual: => R$ {self.saldo} <={colorir["Fecha_Cor"]}')
                        input('Pressione qualquer tecla para voltar ao menu inicial...')   
            
                    case _:
                        print(f'\n{colorir["Vermelho"]}Você já atingiu o limite de saques diários, volte amanhã!{colorir["Fecha_Cor"]}')

                    
            

    def depositar(self, valor: float, hora: str) -> None:
        """_ Método responsável por realizar depósito de valores na conta do usuário
         após fazer algumas validações. _

        Args:
            valor (float): _ Representa o valor a ser depositado informado pelo usuário. _
            hora (str): _ Representa o horário no qual foi realizado a operação de depósito. _
        """
        match valor:

            case _ as valor_invalido if valor_invalido == 0 or valor_invalido < 0:
                print(f'\n{colorir["Vermelho"]}Só é permitido depositar valores positivos!{colorir["Fecha_Cor"]}')

            case _ as quantidade if quantidade >= 1:
                saldo_anterior=self.saldo
                self.saldo += valor
                self.dados_extrato["Quantidade de Depósitos"][0] += 1
                self.dados_extrato["Informações dos Depósitos"]["Valores"].append(valor)
                self.dados_extrato["Informações dos Depósitos"]["Horários"].append(hora)
                print(f'\n{colorir["Laranja"]}O valor de R$ {valor:.2f} foi depositado com sucesso! Confira abaixo os detalhes da operação.{colorir["Fecha_Cor"]}\n')
                print(tabulate({"Saldo Anterior": [saldo_anterior],
                                "Saldo atual":[self.saldo],
                                "Valor depositado":[valor],
                                "Horário do Depósito":[hora]
                                }, headers='keys', tablefmt='fancy_grid', missingval='Célula Vazia'))
                input('Pressione qualquer tecla para voltar ao menu inicial...')
                saldo_anterior = ''
    
    def extrato_deposito(self) -> None:
        """Método responsável por apresentar na tela um extrato contendo todas as operações
        realizadas pelo usuário de forma detalhada.
        """
        data = datetime.today()
        dia = data.date().strftime("%d/%m/%Y")
        print()
        print(f" {colorir['Laranja']}Este é o seu extrato gerado correspondente as operações realizadas na data de: {dia}{colorir['Fecha_Cor']} ".center(130, '='))

        print(tabulate({                   "Quantidade de Saques":[self.dados_extrato["Quantidade de Saques"][0]], 
                                           "Valores dos Saques R$":self.dados_extrato["Informações dos Saques"]["Valores"],
                                           "Horários dos Saques":self.dados_extrato["Informações dos Saques"]["Horários"],
                                           "Quantidade de Depósitos":[self.dados_extrato["Quantidade de Depósitos"][0]], 
                                           "Valores dos Depósitos R$":self.dados_extrato["Informações dos Depósitos"]["Valores"],
                                           "Horários dos Depósitos":self.dados_extrato["Informações dos Depósitos"]["Horários"]
                                           }, headers='keys', tablefmt='fancy_grid', missingval='Célula Vazia'))
        print()
        print(f'Seu saldo atual é de: => R$ {self.saldo:.2f} <=\n')
        input('Pressione qualquer tecla para voltar ao menu!')




class Sistema_Bancario(Operacoes):
    """_ Classe que representa o sistema principal, contendo todas as características
     da conta bancária, e valores. Possui também o método para apresentar o menu princial
      ao usuário. _

    Args:
        Operacoes (_Class_): _ Classe repassada por herança que contêm todos os métodos utilizados
         na classe principal. _
    """
    def __init__(self, menu: list) -> None:
        self.menu = menu
        self.saldo = 0
        self.dados_extrato = {
            "Quantidade de Saques": [0],
            "Informações dos Saques": {"Valores":[], "Horários":[]},
            "Quantidade de Depósitos": [0],
            "Informações dos Depósitos": {"Valores": [], "Horários":[]},
        }


    def menu_principal(self) -> str:
        """_ Método que fornece ao usuário todas as opções
        do menu principal. _

        Returns:
            str: _ Retorna uma das opções do menu escolhidas pelo usuário._
        """
        print(sistem_logo)
        print('\nSeja bem vindo ao nosso Sistema de Operações Bancárias!\n'
              'Versão 1.0\n')
        print(" MENU ".center(40, '='))
        for index, opcao in enumerate(self.menu):
            print(f"[{index+1}] -> {opcao}")
        print("".center(40, '='))

        while True:
            try:
                escolha_do_usuario = input('\nEscolha o procedimento a ser feito digitando\n'
                                           'o número correspondente a opção:  ').strip()

                digitou_letra = any([caracter.isalpha() for caracter in escolha_do_usuario])

                match digitou_letra:
                    case True:
                        raise ValueError(f'\n{colorir["Vermelho"]}ERRO! Digite somente números!{colorir["Fecha_Cor"]}')
                    case _:
                        match escolha_do_usuario:
                            case "":
                                raise ValueError(f'\n{colorir["Vermelho"]}ERRO! Você precisa digitar alguma opção, '
                                                 f'tente novamente.{colorir["Fecha_Cor"]}')
                            case _ as status if  status.isalnum() == False:
                                raise ValueError(f'\n{colorir["Vermelho"]}ERRO! Digite somente números!'
                                                 f'{colorir["Fecha_Cor"]}')
                            case _:
                                escolha_do_usuario = int(escolha_do_usuario)
                                if escolha_do_usuario > 4 or escolha_do_usuario < 1:
                                    raise ValueError(f'\n\n{colorir["Vermelho"]}ERRO! Você digitou uma opção inválida, '
                                                     f'tente novamente.{colorir["Fecha_Cor"]}')

            except ValueError as erro:
                print(erro)
                continue

            else:
                match escolha_do_usuario:
                    case 1:
                        print(f'\n{colorir["Verde"]}Você escolheu a opção -> {self.menu[0]}{colorir["Fecha_Cor"]}')
                        return self.menu[0]
                    case 2:
                        print(f'\n{colorir["Verde"]}Você escolheu a opção -> {self.menu[1]}{colorir["Fecha_Cor"]}')
                        return self.menu[1]
                    case 3:
                        print(f'\n{colorir["Verde"]}Você escolheu a opção -> {self.menu[2]}{colorir["Fecha_Cor"]}')
                        return self.menu[2]
                    case 4:
                        print(f'\n{colorir["Verde"]}Você escolheu a opção -> {self.menu[3]}{colorir["Fecha_Cor"]}')
                        return self.menu[3]


if __name__ == '__main__':
    sistema = Sistema_Bancario(['Depositar', 'Sacar', 'Gerar Extrato', 'Finalizar'])
    

    while True:
        data = datetime.today()
        dia = data.date().strftime("%d/%m/%Y")
        hora = data.time().strftime("%H:%M:%S")

        resposta_usuario = sistema.menu_principal()
        match resposta_usuario:
            case "Depositar":
                valor_deposito = input('Informe o valor do deposito  R$: ').strip()
                try:
                    valor_deposito = float(valor_deposito)
                except Exception:
                    print(f'\n{colorir["Vermelho"]}Digite somente números! Tente novamente.{colorir["Fecha_Cor"]}')
                    input('Pressione qualquer tecla para voltar ao menu...')
                else:
                    sistema.depositar(valor_deposito, hora)

            case "Sacar":
                valor_saque = input('Informe o valor do Saque R$: ').strip()
                try:
                    valor_saque = float(valor_saque)
                except Exception:
                    print(f'\n{colorir["Vermelho"]}Digite somente números! Tente novamente.{colorir["Fecha_Cor"]}')
                    input('Pressione qualquer tecla para voltar ao menu...')
                else:
                    sistema.sacar(valor_saque, sistema.saldo, sistema.dados_extrato["Quantidade de Saques"][0], hora)
            
            case "Gerar Extrato":
                sistema.extrato_deposito()

            case "Finalizar":
                print('Finalizando sistema, obrigado e volte sempre!')
                break
