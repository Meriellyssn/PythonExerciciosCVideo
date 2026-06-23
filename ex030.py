#Crie um programa que leia um número inteiro e
# mostre na tela se ele é PAR ou ÍMPAR.

num = int(input("Me diga um número inteiro qualquer: "))
resultado = num % 2 #o resto de qualquer número par dividido por 2 vai dar '0'/ e o resto que qualquer número impar dividido por 2 vai dar '1'.
if resultado == 0:
    print('O número {} é PAR.'.format(num))
else:
    print('O número é IMPAR.'.format(num))
