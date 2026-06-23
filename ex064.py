print('''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).''')
print('-=-' * 20)

contador = 0
soma = 0
num = int(input('Digite um número [999 para parar]: ')) # para que o flag não seja contador.
while num != 999:
    soma += num
    contador +=1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou >> {} números e a soma entre eles é de >> {}.'.format(contador, soma))
