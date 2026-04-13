#um progra que gera codico de barras
import random
numeros = [random.randint(0, 9) for _ in range(12)]
print(''.join(map(str, numeros)))

