print('''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.''')
print('-=' * 20)
print('{:^40}'.format('COMERCIAL BARATÃO'))
print('-=' * 20)

total = totMil = menor = cont = 0
barato = ''
while True:
    #1 Entrada de Dados
    produto = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço do produto: R$ '))
    cont += 1
    #PRECESSAMENTO DE DADOS
    #A) qual é o total gasto na compra.
    total += preco

    # B) quantos produtos custam mais de R$1000.
    if preco > 1000:
        totMil += 1

    #C) qual é o nome do produto mais barato.
    if cont == 1 or preco < menor:
        menor = preco #Diz o preço do produto
        barato = produto #Diz o nome do produto
    #2 Entrada de Dados
    resp = ' '
    while resp not in 'SN': #Verificação
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

#Saída de Dados
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$:{total:.2f}')
print(f'Temos >> {totMil} << produtos custando mais de R$1000.00')
print(f'O produto mais barato foi  >> {barato} << que custa R$:{menor:.2f}')