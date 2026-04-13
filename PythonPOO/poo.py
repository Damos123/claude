#declaração da classe
class aprendiz:
    def __init__(self, nome, idade):  # construtor
        self.nome = nome
        self.idade = idade

    # metodo de instancia
    def aniversario(self):
        print('Parabens feliz aniversario', self.nome)
        self.idade = self.idade + 1

    def mensagem(self):
        return 'Celebramos o aniversario  juntos com ' + self.nome + ' e ele tem ' + str(self.idade) + ' anos'
# declaração do objetos
aprendiz1 = aprendiz("Alvez", 16)
aprendiz2 = aprendiz("Mariana", 17)

aprendiz1.aniversario()
aprendiz2.aniversario()
print(aprendiz1.mensagem())
print(aprendiz2.mensagem())
