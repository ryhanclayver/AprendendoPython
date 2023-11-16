import math

cOposto = float(input('Digite o cateto oposto: '))
cAdjacente = float(input('Digite o cateto adjacente: '))
print(f'Hipotenusa: {math.hypot(cOposto, cAdjacente):.2f}')