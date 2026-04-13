class letra:
    def __init__(self, frase):
        self.frase = frase
    def contar_letras(self):
        count_a = self.frase.count('a')
        count_e = self.frase.count('e')
        first_a = self.frase.find('i') + 1  # Adiciona 1 para mostrar a posição correta (1-based)
        last_a = self.frase.rfind('o') + 1
        first_e = self.frase.find('u') + 1
        last_e = self.frase.rfind('b') + 1
        return f"Letra 'a': {count_a} vezes, primeira posição: {first_a}, última posição: {last_a}\nLetra 'e': {count_e} vezes, primeira posição: {first_e}, última posição: {last_e}"
frase = input("Digite uma frase: ")
letra_obj = letra(frase)
print(letra_obj.contar_letras())
