"""
Projeto Caixa Eletrônico Bancário

Requisitos

DEPÓSITO:

- Depositar somente valores positivos
- Armazenar o depósito em uma variável
- Exibir dados do depósito em formato de extrato
- Armazenar as informações relacionadas ao depósito como valor, quantidade de depósitos
etc

SAQUE:

- Permitir 3 saques diários Máximo 500 reais por saque. (verificar se existe saldo para o saque).
- Caso o Usuário não tenha saldo em conta, exibir uma mensagem informando
que não será possível sacar o dinheiro por falta de saldo.
- Todas as operações de saque devem ser armazenadas em uma variável.

EXTRATO:

 - Deve listar todos os depósitos e saques realizados na conta. No fim da
listagem, deve ser exibido o saldo atual da conta.
"""

colorir = {
    "Vermelho":'\033[31m',
    'Verde':'\033[32m',
    'Fecha_Cor':'\033[m'
}


class Operacoes:
    def sacar(self, valor):

        match valor:
            case _ as quantidade if quantidade > 0 and quantidade <= 500:
                self.saldo -= valor
                self.dados_extrato["Quantidade de Saques"]+=1
                print(self.saldo)
                print(self.dados_extrato["Quantidade de Saques"])


    def depositar(self, valor):
        match valor:
            case _ as quantidade if quantidade >=1:
                self.saldo += valor
                self.dados_extrato["Quantidade de Depósitos"] +=1
                print(self.saldo)
                print(self.dados_extrato["Quantidade de Depósitos"])          



class Sistema_Bancario(Operacoes):
    def __init__(self, menu: list) -> None:
        self.menu = menu
        self.saldo = 0
        self.dados_extrato = {
            "Quantidade de Saques":0,
            "Valores dos Saques":[],
            "Quantidade de Depósitos":0,
            "Valores dos Depósitos":[],
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
                                raise ValueError(f'\n{colorir["Vermelho"]}ERRO! Você precisa digitar alguma opção, tente novamente.{colorir["Fecha_Cor"]}')
                            case _ as status if  status.isalnum() == False:
                                raise ValueError(f'\n{colorir["Vermelho"]}ERRO! Digite somente números!{colorir["Fecha_Cor"]}')
                            case _:
                                escolha_do_usuario = int(escolha_do_usuario)
                                if escolha_do_usuario > 4 or escolha_do_usuario < 1:
                                    raise ValueError(f'\n\n{colorir["Vermelho"]}ERRO! Você digitou uma opção inválida, tente novamente.{colorir["Fecha_Cor"]}')

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
        resposta_usuario = sistema.menu_principal()
        match resposta_usuario:
            case "Depositar":
                valor_deposito = float(input('Informe o valor do deposito  R$: '))
                sistema.depositar(valor_deposito)
            
            case "Sacar":
                valor_saque = float(input('Informe o valor do Saque R$: '))
                sistema.sacar(valor_saque)
            
            case "Finalizar":
                print('Finalizando sistema, obrigado e volte sempre!')
                break
            
