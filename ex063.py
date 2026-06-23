print('''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os 
N primeiros elementos de uma Sequência de Fibonacci. 
Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8''')
print('-=' * 20)

print('Seguência de Fibonacci')
print('-=' * 20)
n = int(input('Quantos termos você deseja ver? '))
t1 = 0
t2 = 1
print('-=' * 20)
print('{} -> {}'.format(t1, t2), end='') #até aqui exibimos os 2 primeiros termos t1 e t2.
#Agora precisamos exibir o terceiro termo (t3).
contador = 3
while contador <= n:
    t3 = t1 + t2
    print(' -> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' -> FIM')
print('-=' * 20)
