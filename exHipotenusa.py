from math import hypot

cOposto = float(input('Digite o cateto oposto: '))
cAdjacente = float(input('Digite o cateto adjacente: '))
print(f'Hipotenusa: {hypot(cOposto, cAdjacente):.2f}')
