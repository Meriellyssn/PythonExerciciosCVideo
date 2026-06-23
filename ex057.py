print('''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.''')

print('-' * 40)
print('Programa Inicializado...')
print('-' * 40)
sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: '))
print('Sexo {} registrado com sucesso!'.format(sexo))
print('Fim do programa...')