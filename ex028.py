#Escreva um programa que faça o computador “pensar” em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)#Faz o computador sortear um número!
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhas...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei: '))#Jogador tenta adivinha.
print('PROCESSANDO...')
sleep(2)#faz o computador esperar por 2 segundos.
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {}, e não no número {}.'.format(computador, jogador))
