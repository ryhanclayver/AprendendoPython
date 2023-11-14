km = float(input('Digite a quantidade de KM rodados: '))
dia = float(input('Digite a quantidade de dias alugado: '))
preco = (dia * 60.00) + (km * 0.15)
print(f'O valor total a se pagar será: {preco:.2f}')
