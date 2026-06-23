print('''Crie um programa que leia vários números pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag).''')
print('-=' * 20)
contador = soma = 0
while True:
    num = int(input('Digite um valor(999 para parar): '))
    if num == 999:
        break
    soma += num
    contador +=1
print(f'A soma dos {contador} valores foi >> {soma}!')
