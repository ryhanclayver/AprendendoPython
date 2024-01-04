nome = input('Digite o nome da sua cidade: ')
if 'santo' not in nome.split()[0] and 'Santo' not in nome.split()[0] and 'SANTO' not in nome.split()[0]:
    print('O nome da sua cidade não começa com Santo')
else:
    print('O nome da sua cidade começa com Santo')
