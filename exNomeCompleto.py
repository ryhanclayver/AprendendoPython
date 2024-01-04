nome = input("Digite o seu nome completo: ")
print(f'Primeiro nome: {nome.split()[0]}')
print(f'Segundo nome: {nome.rsplit(maxsplit=1)[1]}')

