print('''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.''')
print('-=' * 20)
lista = []
for cont in range(0,5):
    num = int(input('Digite um valor: '))
    if cont == 0 or num > lista[-1]:
        lista.append(num)
        print('Valor adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print('-=' * 20)
print(f'Os valores digitados em ordem foram {lista}')
print('-=' * 20)
