distancia = float(input("Digite a distância da viagem em km: "))
if distancia <= 200:
    preco = distancia * 2.50
else:
    preco = distancia * 5.00
print(f"O preço da passagem é: €{preco:.2f}")
