print('''Crie um programa que tenha uma dupla totalmente preenchida com 
uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado 
(entre 0 e 20) e mostrá-lo por extenso.''')
print('-=' * 20)

cont = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO',
        'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE',
        'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE',
        'QUINZE', 'DEZESEIS', 'DEZESETE', 'DEZOITO',
        'DEZENOVE', 'VINTE')

#ENTRADA DE DADOS
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print('-=' * 20)
        print(f'Você digitou o número >> {cont[num]}')
    else:
        print('Número Inválido! Tente novamente. ', end='')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('- FIM DO PROGRAMA -')