print('''Crie um programa que vai gerar cinco números aleatórios 
e colocar em uma tupla. Depois disso, mostre a listagem de 
números gerados e também indique o menor e o 
maior valor que estão na tupla.''')
print('-=' * 20)
from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print('\n')
print('-=' * 20)
print(f'O maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')
print('-=' * 20)