a = float(input('Digite o comprimento do primeiro lado: '))
b = float(input('Digite o comprimento do segundo lado: '))
c = float(input('Digite o comprimento do terceiro lado: '))
if a < b + c and b < a + c and c < a + b:
    print('Os lados formam um triângulo')
else:    print('Os lados não formam um triângulo')