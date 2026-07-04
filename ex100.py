print('''Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar 
a soma entre todos os valores pares sorteados pela função anterior.''')
print('-=' * 20)

from random import randint
from time import sleep

numeros = list()

def sorteia(lista):
    print('Sorteando os valores da lista: ', end='')
    for cont in range(5):
        n = randint(1, 9)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO!')

def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da lista {lista}, temos = {soma}.')

#Programa principal
sorteia(numeros)
soma_par(numeros)