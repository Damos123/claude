#Criei um programa que lê o nome completo de uma pessoa e mostre:em seguida, o primeiro nome, o último nome separadamente
class nome:
    def __init__(self, nome_completo):
        self.nome_completo = nome_completo
    def separar_nome(self):
        nomes = self.nome_completo.split()
        primeiro_nome = nomes[0]
        ultimo_nome = nomes[-1]
        return f"Primeiro nome: {primeiro_nome}, Último nome: {ultimo_nome}"
nome_completo = input("Digite o nome completo: ")
nome_obj = nome(nome_completo)
print(nome_obj.separar_nome())
