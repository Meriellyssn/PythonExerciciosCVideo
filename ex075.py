print('''Desenvolva um programa que leia quatro valores pelo 
teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.''')
print('-=' * 20)
valores = (int(input('Digite o 1º valor: ')),
           int(input('Digite o 2º valor: ')),
           int(input('Digite o 3º valor: ')),
           int(input('Digite o 4º valor: ')))
print('-=' * 20)
print(f'Você digitou os valores {valores}')
#A) Quantas vezes apareceu o valor 9.
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
#B) Em que posição foi digitado o primeiro valor 3.
if 3 in valores:
    print(f'O número 3 apareceu na {valores.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nem uma posição!')
#C) Quais foram os números pares.
print('Os valores pares digitados foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')