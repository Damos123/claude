velocidade = float(input("Digite a velocidade do carro em km/h: "))
limite = 80
multa = (velocidade - limite) * 7
if velocidade > limite:
    print(f"Você foi multado! Sua velocidade estava {velocidade - limite:.2f} km/h acima do limite.")
    print(f"O valor da multa é: {multa:.2f}€")
else:    print("Parabéns! Você está dentro do limite de velocidade.")
