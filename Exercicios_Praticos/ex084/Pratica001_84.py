lista_temp = []
lista_princ = []
maior = menor = 0
while True:
    #Entrada de Dados
    lista_temp.append(str(input('Nome do Produto: ')))
    lista_temp.append(float(input('Preço do Produto: R$')))
    #Verificação do maior e menor preço.
    if len(lista_princ) == 0:
        maior = menor = lista_temp[1]
    else:
        if lista_temp[1] > maior:
            maior = lista_temp[1]
        if lista_temp[1] < menor:
            menor = lista_temp[1]

    lista_princ.append(lista_temp[:])
    lista_temp.clear()

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break

print('-=' * 20)
#Quantos produtos foram cadastrados no total.
print(f'O total de produtos cadastrados foram: {len(lista_princ)} produtos.')
#Qual foi o maior preço registrado e o nome do(s) produto(s) que custam esse valor.
print(f'O maior preço foi de R${maior:.2f}. Do(s) produto(s): ', end='')
for preco in lista_princ:
    if preco[1] == maior:
        print(f'[{preco[0]}] ', end='')
print()
#Qual foi o menor preço registrado e o nome do(s) produto(s) que custam esse valor.
print(f'O menor preço foi de R${menor:.2f}. Do(s) produto(s): ', end='')
for preco in lista_princ:
    if preco[1] == menor:
        print(f'[{preco[0]}] ', end='')
print()
print('-=' * 20)
