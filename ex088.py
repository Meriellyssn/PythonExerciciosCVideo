print('''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.''')


from random import randint
from time import sleep

lista = list()
jogos = list()
print('-=' * 20)
print(' ' * 8, 'JOGA NA MEGA SENA', ' ' * 8)
print('-=' * 20)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= quant:
    contador = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 3, f' SORTEADO {quant} JOGOS', '-=' * 3)
for indice, lis in enumerate(jogos):
    print(f'Jogo {indice + 1}: {lis}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)