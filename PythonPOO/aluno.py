# crie um programa que lê nome de uma pessoa e mostra o nome com todas as letras maiusculas 
# e minusculas e quantas letras ao todo (sem considerar espacos e quantas letras tem o primeiro nome
class aluno:
    def __init__(self, nome):
        self.nome = nome
    def maiusculo(self):
        return self.nome.upper()
    def minusculo(self):        return self.nome.lower()
    def contar_letras(self):
        return len(self.nome.replace(" ", ""))
    def contar_letras_primeiro_nome(self):        return len(self.nome.split()[0])
nome = input("Digite o nome do aluno: ")
aluno = aluno(nome)
print(f"Nome em maiusculo: {aluno.maiusculo()}")
print(f"Nome em minusculo: {aluno.minusculo()}")
print(f"Quantidade de letras: {aluno.contar_letras()}")
print(f"Quantidade de letras do primeiro nome: {aluno.contar_letras_primeiro_nome()}")  
