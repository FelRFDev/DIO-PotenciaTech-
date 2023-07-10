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

class Sistema_Bancario:
    def __init__(self, menu: list):
        self.menu = menu

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
                match escolha_do_usuario:
                    case "":
                        raise ValueError('\nERRO! Você precisa digitar alguma opção, tente novamente.')
                    case _:
                        escolha_do_usuario = int(escolha_do_usuario)
                        if escolha_do_usuario > 4 or escolha_do_usuario < 1:
                            raise ValueError('\nERRO! Você digitou uma opção inválida, tente novamente.')

            except ValueError as erro:
                print(erro)
                continue

            else:
                match escolha_do_usuario:
                    case 1:
                        print(f'\nVocê escolheu a opção -> {self.menu[0]}')
                        return self.menu[0]
                    case 2:
                        print(f'\nVocê escolheu a opção -> {self.menu[1]}')
                        return self.menu[1]
                    case 3:
                        print(f'\nVocê escolheu a opção -> {self.menu[2]}')
                        return self.menu[2]
                    case 4:
                        print(f'\nVocê escolheu a opção -> {self.menu[3]}')
                        return self.menu[3]

if __name__ == '__main__':
    sistema = Sistema_Bancario(['Depositar', 'Sacar', 'Gerar Extrato', 'Finalizar'])
    usuario = sistema.menu_principal()
