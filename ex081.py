print(''' Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:                          A) Quantos números foram digitados.             B) A lista de valores, ordenada de forma decrescente.                                    C) Se o valor 5 foi digitado e está ou não na lista.''')
print('-=' * 20)
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 20)
#A) Quantos números foram digitados.
print(f'Você digitou {len(valores)} elementos.')
#B) A lista de valores, ordenada de forma decrescente.
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
#C) Se o valor 5 foi digitado e está ou não na lista.
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
print('-=' * 20)