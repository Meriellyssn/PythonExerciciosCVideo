print('''Faça um loop "for" que passe por todos os
preços e aplique um desconto de 10% em cada um,
salvando em uma nova lista chamada "preco_com_desconto".
Imprima o valor total(soma) da lista original e da lista
com desconto(dica: pesquise sobre a função nativa sum()''')
print('-=' * 20)
produtos = [
    'Arroz 5kg', 25.90,
    'Feijão 1kg', 8.90,
    'Óleo de soja', 6.20,
    'Açúcar 2kg', 8.50,
    'Detergente', 1.79,
    'Amaciante', 10.90,
    'Papel Higiênico', 12.85,
    'Desodorante Dove', 15.90,
    'Absorvente', 13.50,
    'Leite em pó', 8.90
]
preco_com_desconto = []
precos = []
print('LISTA DE PREÇOS'.center(40))
print('-=' * 20)

for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<30}', end='')
    else:
        print(f'{produtos[posicao]:>7.2f}')
        precos.append(produtos[posicao])
        preco_com_desconto.append(produtos[posicao] - (produtos[posicao] * 0.10))
print(f'Valor total ............... R${sum(precos):>7.2f}')
print('-=' * 20)
print('LISTA DE PREÇOS COM 10% DE DESCONTO'.center(40))
print('-=' * 20)
for i in range(0, len(preco_com_desconto)):
    print(f'{produtos[i * 2]:.<30}', end='')
    print(f'{preco_com_desconto[i]:>7.2f}')
print(f'Valor total ............... R${sum(preco_com_desconto):>7.2f}')