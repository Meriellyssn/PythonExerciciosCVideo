#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#1 opção
import math
num = float(input('Digite um numero: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num, math.trunc(num)))

#2 opção
from math import trunc
num = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num, trunc(num)))

#3 opção
num = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num, int(num)))
