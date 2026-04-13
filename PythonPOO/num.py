class numero:
    def __init__(self, num):
        self.num = num
    def separar_digitos(self):
        num_str = str(self.num).zfill(4)  # Preenche com zeros à esquerda para garantir 4 dígitos
        return f"Unidade: {num_str[3]}, Dezena: {num_str[2]}, Centena: {num_str[1]}, Milhar: {num_str[0]}"
num = int(input("Digite um número : "))
if 0 <= num <= 9999:
    numero_obj = numero(num)
    print(numero_obj.separar_digitos())
else:
    print("Número inválido. Por favor, digite um número entre 0 e 9999.")
