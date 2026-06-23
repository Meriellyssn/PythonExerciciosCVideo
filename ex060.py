print('''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120''')
print('-=' * 20)
print('Calculando o fatorial.')
print('-=' * 20)
'''from math import factorial #opção usando modulo
n = int(input('Digite um número para calcular o Fatorial: '))
f = factorial(n)
print('O fatorial de {} é >> {}.'.format(n, f))'''

#fazendo de forma tradicional
n = int(input('Digite um número para calcular seu Fatorial: '))
contador = n
fact = 1
print('Calculando o {}! = '.format(n), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fact *= contador
    contador -= 1
print('{}'.format(fact))

#fatorial usando for quando se saber o valor de 'n'.
'''n = int(input('Digite o número 5 para calcular o fatorial: '))
fact = 1
print('Calculando o {}! = '.format(n), end='')
for n in range(5, 0, -1):
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    fact *= n
print('{}'.format(fact))'''
