print('''Crie um programa que tenha uma tupla única 
com nomes de produtos e seus respectivos preços, 
na sequência. No final, mostre uma listagem de preços,
organizando os dados em forma tabular.''')
print('-=' * 20)
listagem = ('Lápis', 1.75,
            'Borracha', 1.50,
            'Caderno', 15.00,
            'Estojo', 25.00,
            'Transferidor', 2.00,
            'Compasso', 9.00,
            'Mochila', 90.00,
            'Canetas', 20.00,
            'Livro', 34.90)
print('-=' * 20)
print(f'LISTAGEM DE PREÇOS' .center(40))
print('-=' * 20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')#Colocando os itens a esquerda "<".
    else:
        print(f'R${listagem[pos]:> 7.2f}')#Colocando os itens a direita ">".
print('-=' * 20)
