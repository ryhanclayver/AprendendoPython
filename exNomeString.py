nome = str(input('Digite o nome: ')).strip()
print(f'seu nome em maiuculas é {nome.upper()}')
print(f'seu nome em minusculas é {nome.lower()}')
print(f'seu nome ao todo tem {len(nome) - nome.count(' ')} letras')
primeiroNome = nome.split()[0]
print(f'tamanho do primeiro nome é {len(primeiroNome)}')





