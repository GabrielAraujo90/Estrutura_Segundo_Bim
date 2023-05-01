#Gabriel Araujo
#Atividade 01

class ContaBancaria:
    def __init__(self, numero_conta, nome_pessoa, saldo):
        self.numero_conta = numero_conta
        self.nome_pessoa = nome_pessoa
        self.saldo = saldo

    def depositar(self):
        valor = float(input("Digite o valor a ser depositado: "))
        self.saldo += valor
        print(f"Depósito realizado com sucesso. Novo saldo: R${self.saldo:.2f}")

    def sacar(self):
        valor = float(input("Digite o valor a ser sacado: "))
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque realizado com sucesso. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def imprimir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


minha_conta = ContaBancaria(12345, "Gabriel Araujo", 500.0)

opcao = 0
while opcao != 4:
    print("\nSelecione uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Imprimir saldo")
    print("4 - Sair")
    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        minha_conta.depositar()
    elif opcao == 2:
        minha_conta.sacar()
    elif opcao == 3:
        minha_conta.imprimir_saldo()
    elif opcao == 4:
        print("Encerrando a conta...")
    else:
        print("Opção inválida. Tente novamente.")
