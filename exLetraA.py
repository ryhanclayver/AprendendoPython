frase = input('Digite uma frase: ')
a = frase.count('a')+frase.count('A')
print(f'Apareceram {a} letras "A"')
print(f'Ela aparece pela primeira vez na posição {frase.find('a')}')
print(f'Ela aparece pela última vez na posição {frase.rfind('a')}')