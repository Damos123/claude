import random
class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo_inicial):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de €{valor} realizado com sucesso. Saldo atual: €{self.saldo}")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            print(f"Saque de €{valor} realizado com sucesso. Saldo atual: €{self.saldo}")

    def consultar_saldo(self):
        print(f"Saldo atual da conta: €{self.saldo}")
# Solicitar informações do usuário para criar a conta quero gerar numero da conta automaticamente, por exemplo, usando um contador ou um número aleatório

nome_completo = input("Nome completo: ")
nome_pai = input("Nome do pai: ")
nome_mae = input("Nome da mãe: ")
saldo_inicial = float(input(" Valor inicial para depósito: "))
numero_conta = random.randint(1000, 9999)

# Criar a conta bancária
conta = ContaBancaria(nome_completo, numero_conta, saldo_inicial)

# Mostrar informações da conta
print("Informações da conta:")
print(f"Titular: {conta.titular}")
print(f"Número da conta: {conta.numero_conta}")
print(f"Saldo inicial: €{conta.saldo}")
valor_saque = float(input("Queres lavar o dinheiro?\nValor para saque: "))
conta.sacar(valor_saque)
valor_deposito = float(input("Valor para depósito: "))
conta.depositar(valor_deposito)
conta.consultar_saldo()









 



   





