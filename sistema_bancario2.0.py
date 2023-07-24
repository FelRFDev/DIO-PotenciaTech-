
"""
Desafio parte 2 - Refatorando o código!

- Separar as funções existentes de saque depósito e extrato em Funções! Cada função deverá ter uma regra
na passagem de argumentos.

* A função de saque deve receber argumentos somente por **Kwargs. #### => FEITO <= ####
* A função de depósito deve receber os argumentos somente por posição. #### => FEITO <= ####
* A função de extrato deve receber os argumentos de forma posicional e **kwargs (Argumento posicional: saldo / Argumento Nomeado: Extrato) #### => FEITO <= ####


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

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Modificações feitas =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


Para a função de extrato, foi acrescentado um menu fornecendo mais de um tipo de extrato:

 - Extrato para saques
 - Extrato para depósitos
 - Extrato Geral/Completo

As opções são repassadas a função conforme solicitado no exercício.

"""

from datetime import datetime
from tabulate import tabulate

sistem_logo = """███████╗██╗███████╗████████╗███████╗███╗   ███╗ █████╗                            
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
    "Vermelho": '\033[31m',
    'Verde': '\033[32m',
    'Fecha_Cor': '\033[m',
    "Laranja": '\033[34m'
}


class Usuario:
    def __init__(self, nome: str, data_nascimento: int, cpf: int, endereco: str) -> None:
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.dados_usuario = {key: value for (key, value) in self.__dict__.items()}

    def __str__(self):
        return f'Class: {self.__class__.__name__} - Atributtes: {", ".join([f"{key}: {value}" for (key, value) in self.__dict__.items()])}'


class Operacoes:
    """_ Classe resposnável por conter as principais funcionalidades do sistema principal. _
    """

    def cadastrar_usuario(self):

        confirmar_dados = False
        while confirmar_dados == False:
            # ========== Início da Etapa 1 ==========
            print()
            print(' CADASTRAMENTO - ETAPA 1 (IDENTIFICAÇÃO) '.center(80, "="))
            nome_do_usuario = input(
                '\nPor favor, digite o nome completo do usuário ou "sair" para voltar ao menu: ').strip().title()
            if nome_do_usuario == 'Sair':
                break
            elif True in [any(letra.isdigit() for letra in nome_do_usuario)] or not nome_do_usuario:
                print(f'\n{colorir["Vermelho"]}Informação inválida! Tente novamente.{colorir["Fecha_Cor"]}')
            else:
                while True:
                    data_nascimento = input('Informe a data de nascimento: ').strip()
                    if not data_nascimento:
                        print(f'\n{colorir["Vermelho"]}Informação inválida! Tente novamente.{colorir["Fecha_Cor"]}')
                        continue
                    else:
                        while True:
                            cpf = input("Informe os números do cpf. DIGITE SOMENTE OS NÚMEROS:").strip()
                            try:
                                cpf = int(cpf)
                            except Exception:
                                print(
                                    f'\n{colorir["Vermelho"]}Informação inválida! Tente novamente.{colorir["Fecha_Cor"]}')
                                continue
                            else:
                                print(
                                    '\nDeseja confirmar as informações para Identificação e prosseguir para a segunda etapa?')
                                prosseguir = input('Digite Sim ou Não para voltar ao início: ').strip().title()
                                if prosseguir == 'Não':
                                    break
                                else:
                                    # ========== Início da Etapa 2 ==========
                                    print()
                                    print(' CADASTRAMENTO - ETAPA 2 (RESIDÊNCIA) '.center(80, "="))
                                    confirmar_endereco = False
                                    endereco = ''
                                    while confirmar_endereco == False:
                                        logradouro = input('Informe o  Logradouro: ').strip()
                                        if not logradouro:
                                            print(
                                                f'\n{colorir["Vermelho"]}Informação inválida! Tente novamente.{colorir["Fecha_Cor"]}')
                                            continue
                                        numero = input('Informe o número da residência: ').strip()
                                        try:
                                            numero = int(numero)
                                        except Exception:
                                            print(
                                                f'\n{colorir["Vermelho"]}Informação inválida! Tente novamente.{colorir["Fecha_Cor"]}')
                                            continue
                                        else:
                                            bairro = input('Informe o bairro: ').strip()
                                            if not bairro:
                                                print(
                                                    f'\n{colorir["Vermelho"]}Informação inválida! Tente novamente.{colorir["Fecha_Cor"]}')
                                                continue
                                            cidade = input('Informe a cidade: ').strip()
                                            estado = input('Informe o estado: ')
                                            if not cidade or not estado:
                                                print(
                                                    f'\n{colorir["Vermelho"]}Informação inválida! Tente novamente.{colorir["Fecha_Cor"]}')
                                                continue
                                            print(
                                                '\nDeseja confirmar as informações para Residência e prosseguir para a etapa final?')
                                            confirmar = input(
                                                'Digite Sim ou Não para voltar ao início: ').strip().title()

                                            if confirmar == 'Sim':
                                                # ========== Início da Etapa 3 ==========
                                                endereco = f'Logradouro: {logradouro} / Número: {numero}/ Bairro: {bairro} / {cidade}-{estado}'
                                                confirmar_endereco = True
                                                print()
                                                print(' CADASTRAMENTO - ETAPA 3 (CONCLUIR CADASTRO) '.center(80, "="))
                                                print(
                                                    '\nAo concluir o cadastro, você concorda estar ciente e declara ser reponsável por todos os dados informados nas etapas anteriores.')
                                                print(
                                                    '\nDeseja confirmar as informações de todas as etapas anteriores e concluir o cadastro?')
                                                confirmar_dados = input(
                                                    'Digite Sim ou Não para voltar ao início: ').strip().title()
                                                if confirmar_dados == 'Sim':
                                                    novo_usuario = Usuario(nome_do_usuario, data_nascimento, cpf,
                                                                           endereco)
                                                    self.usuarios_cadastrados.append(novo_usuario)
                                                    print(self.usuarios_cadastrados)
                                                    print(novo_usuario)
                                                    print(
                                                        f'{colorir["Verde"]}\n\nUsuário cadastrado com sucesso!{colorir["Fecha_Cor"]}')
                                                    input('Pressione qualquer tecla para voltar ao menu inicial!')
                                                    confirmar_dados = True
                                                else:
                                                    input(
                                                        f'{colorir["Vermelho"]}\n\nCadastramento cancelado, pressione qualquer tecla para voltar ao menu inicial...{colorir["Fecha_Cor"]}')
                                break
                        break

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
                input('Pressione qualquer tecla para voltar ao menu...')

            case _:
                match valor:
                    case _ as positivo if positivo == 0 or positivo < 0:
                        print(f'\n{colorir["Vermelho"]}Só é permitido valores positivos!{colorir["Fecha_Cor"]}')
                        input('Pressione qualquer tecla para voltar ao menu...')

                    case _ as quantidade if quantidade > 500:
                        print(f'\n{colorir["Vermelho"]}Só é permitido sacar valores até R$500,00. Tente novamente!'
                              f'{colorir["Fecha_Cor"]}')

                        input('Pressione qualquer tecla para voltar ao menu...')

                    case _ as quantidade if quantidade > 0 and quantidade <= 500 and saldo > 0 and qtd_saque < 3:
                        self.saldo -= valor
                        self.dados_extrato["Quantidade de Saques"][0] += 1
                        self.dados_extrato["Informações dos Saques"]["Valores"].append(valor)
                        self.dados_extrato["Informações dos Saques"]["Horários"].append(hora)
                        print(f'\n{colorir["Laranja"]}O valor de R$ {valor:.2f} foi sacado com sucesso! '
                              f'Saldo atual: => R$ {self.saldo} <={colorir["Fecha_Cor"]}')
                        input('Pressione qualquer tecla para voltar ao menu inicial...')

                    case _:
                        print(
                            f'\n{colorir["Vermelho"]}Você já atingiu o limite de '
                            f'saques diários, volte amanhã!{colorir["Fecha_Cor"]}')

                        input('Pressione qualquer tecla para voltar ao menu...')

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
                input('Pressione qualquer tecla para voltar ao menu...')

            case _ as quantidade if quantidade >= 1:
                saldo_anterior = self.saldo
                self.saldo += valor
                self.dados_extrato["Quantidade de Depósitos"][0] += 1
                self.dados_extrato["Informações dos Depósitos"]["Valores"].append(valor)
                self.dados_extrato["Informações dos Depósitos"]["Horários"].append(hora)
                print(f'\n{colorir["Laranja"]}O valor de R$ {valor:.2f} foi depositado com sucesso! '
                      f'Confira abaixo os detalhes da operação.{colorir["Fecha_Cor"]}\n')
                print(tabulate({"Saldo Anterior": [saldo_anterior],
                                "Saldo atual": [self.saldo],
                                "Valor depositado": [valor],
                                "Horário do Depósito": [hora]
                                }, headers='keys', tablefmt='fancy_grid', missingval='Célula Vazia'))
                input('Pressione qualquer tecla para voltar ao menu inicial...')
                saldo_anterior = ''

    def extrato(self, saldo: float, extrato: int = '') -> None:
        """Método responsável por apresentar na tela um extrato contendo todas as operações
        realizadas pelo usuário de forma detalhada.
        """
        match extrato:
            case 1:  # saques
                data = datetime.today()
                dia = data.date().strftime("%d/%m/%Y")
                print()
                print()
                print(
                    f"{colorir['Laranja']} Este é o seu extrato gerado correspondente as operações de Saques realizadas na "
                    f"data de: {dia} {colorir['Fecha_Cor']}".center(120, '='))
                print(tabulate({"Quantidade de saques": [self.dados_extrato['Quantidade de Saques'][0]],
                                "Valores dos Saques": self.dados_extrato['Informações dos Saques']['Valores'],
                                "Horário dos Saques": self.dados_extrato['Informações dos Saques']['Horários'],
                                }, headers='keys', tablefmt='fancy_grid', missingval='Célula Vazia'))
                print(f'\nSeu saldo atual é de: => R$ {saldo:.2f} <=\n')
                input('Pressione qualquer tecla para voltar ao menu!')

            case 2:  # depósitos
                data = datetime.today()
                dia = data.date().strftime("%d/%m/%Y")
                print()
                print()
                print(
                    f"{colorir['Laranja']} Este é o seu extrato gerado correspondente as operações de Depósito realizadas na "
                    f"data de: {dia} {colorir['Fecha_Cor']}".center(120, '='))
                print(tabulate({
                    "Quantidade de Depósitos": [self.dados_extrato['Quantidade de Depósitos'][0]],
                    "Valores dos Depósitos": self.dados_extrato['Informações dos Depósitos']['Valores'],
                    "Horário dos Depósitos": self.dados_extrato['Informações dos Depósitos']['Horários'],
                }, headers='keys', tablefmt='fancy_grid', missingval='Célula Vazia'))

                print(f'\nSeu saldo atual é de: => R$ {saldo:.2f} <=\n')
                input('Pressione qualquer tecla para voltar ao menu!')

            case 3:  # completo
                data = datetime.today()
                dia = data.date().strftime("%d/%m/%Y")
                print()
                print(f" {colorir['Laranja']}Este é o seu extrato gerado correspondente as operações realizadas na "
                      f"data de: {dia}{colorir['Fecha_Cor']} ".center(130, '='))

                print(tabulate({"Quantidade de Saques": [self.dados_extrato["Quantidade de Saques"][0]],
                                "Valores dos Saques R$": self.dados_extrato["Informações dos Saques"]["Valores"],
                                "Horários dos Saques": self.dados_extrato["Informações dos Saques"]["Horários"],
                                "Quantidade de Depósitos": [self.dados_extrato["Quantidade de Depósitos"][0]],
                                "Valores dos Depósitos R$": self.dados_extrato["Informações dos Depósitos"]["Valores"],
                                "Horários dos Depósitos": self.dados_extrato["Informações dos Depósitos"]["Horários"]
                                }, headers='keys', tablefmt='fancy_grid', missingval='Célula Vazia'))
                print()
                print(f'Seu saldo atual é de: => R$ {saldo:.2f} <=\n')
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
        self.menu = menu  # lista que contém as opções para o menu
        self.saldo = 0
        self.dados_extrato = {
            "Quantidade de Saques": [0],
            "Informações dos Saques": {"Valores": [], "Horários": []},
            "Quantidade de Depósitos": [0],
            "Informações dos Depósitos": {"Valores": [], "Horários": []},
        }
        self.usuarios_cadastrados = []  # lista para armazenar os usuários cadastrados

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
            print(f"[{index + 1}] -> {opcao}")
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
                            case _ as status if status.isalnum() == False:
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
                    case 5:
                        print(f'\n{colorir["Verde"]}Você escolheu a opção -> {self.menu[4]}{colorir["Fecha_Cor"]}')
                        return self.menu[4]


if __name__ == '__main__':
    sistema = Sistema_Bancario(['Cadastrar Usuário', 'Depositar', 'Sacar', 'Gerar Extrato', 'Finalizar'])

    while True:
        data = datetime.today()
        dia = data.date().strftime("%d/%m/%Y")
        hora = data.time().strftime("%H:%M:%S")

        resposta_usuario = sistema.menu_principal()
        match resposta_usuario:
            case "Cadastrar Usuário":
                sistema.cadastrar_usuario()

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
                extratos_opcs = ['Saques', 'Depósitos', 'Geral']
                print(" Opções de Extrato ".center(40, '='))
                for indice, extrato in enumerate(extratos_opcs):
                    print(f'[{indice + 1}] -> {extrato}')
                print("".center(40, '='))
                tipo_extrato = input('\nEscolha qual tipo de extrado deseja visualizar: ').strip()
                try:
                    tipo_extrato = int(tipo_extrato)
                except Exception:
                    print(f'\n{colorir["Vermelho"]}Opção inválida! Tente novamente.{colorir["Fecha_Cor"]}')
                    input('Pressione qualquer tecla para voltar ao menu...')
                else:
                    sistema.extrato(sistema.saldo, extrato=tipo_extrato)

            case "Finalizar":
                print('Finalizando sistema, obrigado e volte sempre!')
                break
