import random
num = random.randint(0, 10)
print(num)
while True:
    user_input = int(input("Digite um número entre 0 e 10: "))
    if user_input == num:
        print("Parabéns! Você acertou o número!")
        break
    else:
        print("Errado! Tente novamente.")
        continue    
        