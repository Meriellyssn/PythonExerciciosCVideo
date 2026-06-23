print('''Faça um programa que leia 5 valores 
numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o
menor valor digitado e as suas respectivas
posições na lista.''')
print('-' * 40)
listanum = []
maior = 0
menor = 0
for cont in range(5):
    listanum.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = listanum[cont]
    else:
        if listanum[cont] > maior:
            maior = listanum[cont]
        if listanum[cont] < menor:
            menor = listanum[cont]

print('-=' * 20)
print(f'Você digitou os valores: {listanum}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for index, valor in enumerate(listanum):
    if valor == maior:
        print(f'{index}...', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for index, valor in enumerate(listanum):
    if valor == menor:
        print(f'{index}...', end='')
print()
print('-=' * 20)