import random

nome1 = input('Nome do primeiro aluno: ')
nome2 = input('Nome do segundo aluno: ')
nome3 = input('Nome do terceiro aluno: ')
nome4 = input('Nome do quarto aluno: ')

sorteado = [nome1, nome2, nome3, nome4]
random.shuffle(sorteado)

print(f'Nomes na ordem: {sorteado}')


