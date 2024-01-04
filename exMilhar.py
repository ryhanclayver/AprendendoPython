num = input('Digite um número de 0 à 9999: ')

num = num.zfill(4)

print(f'Milhar: {num[0]}')
print(f'Centena: {num[1]}')
print(f'Dezena: {num[2]}')
print(f'Unidade: {num[3]}')
