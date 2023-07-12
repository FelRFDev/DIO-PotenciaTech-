"""
Projeto Caixa Eletrônico Bancário

Requisitos

DEPÓSITO:

- Depositar somente valores positivos ## FEITO ##
- Armazenar o depósito em uma variável  ## Feito ##
- Exibir dados do depósito em formato de extrato 
- Armazenar as informações relacionadas ao depósito como valor, quantidade de depósitos
etc. ## Feito ##

SAQUE:

- Permitir 3 saques diários Máximo 500 reais por saque. (verificar se existe saldo para o saque). ## Feito ##
- Caso o Usuário não tenha saldo em conta, exibir uma mensagem informando
que não será possível sacar o dinheiro por falta de saldo. ## FEITO ##
- Todas as operações de saque devem ser armazenadas em uma variável. ## Feito ##

EXTRATO:
 - Deve listar todos os depósitos e saques realizados na conta. No fim da
listagem, deve ser exibido o saldo atual da conta.
"""

from datetime import datetime
from tabulate import tabulate

colorir = {
    "Vermelho":'\033[31m',
    'Verde':'\033[32m',
    'Fecha_Cor':'\033[m',
    "Laranja": '\033[34m'
}

class Operacoes:
    def sacar(self, valor, saldo, qtd_saque, hora):
        match saldo:
            case 0:
                print(f'\n{colorir["Vermelho"]}Você não possui saldo suficiente para sacar!{colorir["Fecha_Cor"]}')

            case _ :
                match valor:
                    case _ as positivo if positivo == 0 or positivo < 0:
                        print(f'\n{colorir["Vermelho"]}Só é permitido valores positivos!{colorir["Fecha_Cor"]}')

                    case _ as quantidade if quantidade > 0 and quantidade <= 500 and saldo > 0 and qtd_saque < 3:
                        self.saldo -= valor
                        self.dados_extrato["Quantidade de Saques"][0] += 1
                        self.dados_extrato["Informações dos Saques"]["Valores"].append(valor)
                        self.dados_extrato["Informações dos Saques"]["Horários"].append(hora)
                        print(self.saldo)
                        print(self.dados_extrato["Quantidade de Saques"])
                        print(self.dados_extrato["Informações dos Saques"]["Valores"])
                        print(self.dados_extrato["Informações dos Saques"]["Horários"])
                    
                    case _ as quantidade if quantidade > 500:
                        print(f'\n{colorir["Vermelho"]}Só é permitido sacar valores até R$500,00. Tente novamente!{colorir["Fecha_Cor"]}')
            
                    case _:
                        print(f'\n{colorir["Vermelho"]}Você já atingiu o limite de saques diários, volte amanhã!{colorir["Fecha_Cor"]}')
            

    def depositar(self, valor, hora):
        match valor:

            case _ as valor_invalido if valor_invalido == 0 or valor_invalido < 0:
                print(f'\n{colorir["Vermelho"]}Só é permitido depositar valores positivos!{colorir["Fecha_Cor"]}')

            case _ as quantidade if quantidade >= 1:
                self.saldo += valor
                self.dados_extrato["Quantidade de Depósitos"][0] += 1
                self.dados_extrato["Informações dos Depósitos"]["Valores"].append(valor)
                self.dados_extrato["Informações dos Depósitos"]["Horários"].append(hora)
                print(self.saldo)
                print(self.dados_extrato["Quantidade de Depósitos"])
                print(self.dados_extrato["Informações dos Depósitos"]["Valores"])
                print(self.dados_extrato["Informações dos Depósitos"]["Horários"])
    
    def extrato_deposito(self):
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
        input('Pressione qualquer tecla para voltar ao menu!')




class Sistema_Bancario(Operacoes):
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
                valor_deposito = float(input('Informe o valor do deposito  R$: '))
                sistema.depositar(valor_deposito, hora)

            case "Sacar":
                valor_saque = float(input('Informe o valor do Saque R$: '))
                sistema.sacar(valor_saque, sistema.saldo, sistema.dados_extrato["Quantidade de Saques"][0], hora)
            
            case "Gerar Extrato":
                sistema.extrato_deposito()

            case "Finalizar":
                print('Finalizando sistema, obrigado e volte sempre!')
                break



