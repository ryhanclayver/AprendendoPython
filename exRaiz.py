# Crie um algoritmo que leia um número e
# mostre seu dobro, triplo e raiz quadrada

n1 = int(input('Digite um número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)

print('Dobro: {}\nTriplo: {}\nRaiz: {:.2f}'.format(dobro, triplo, raiz))

