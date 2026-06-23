print('''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues. 
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.''')
print('-=' * 20)
print('{:^40}'.format('BANCO CEV '))
print('-=' * 20)

#Entrada de Dados
valor = int(input('Qual o valor do saque? R$: '))

#Processamento
total = valor
cedula = 50 #Comaça com a maior cedula.
contcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        contcedula += 1

    else:
        if contcedula > 0:
            #Saída de Dados
            print(f'Total de {contcedula} cédulas de R$: {cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contcedula = 0
        if total == 0:
            break
