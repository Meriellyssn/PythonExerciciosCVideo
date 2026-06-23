preco = float(input('Qual o valor do produto? R$'))
avista = preco - (preco * 10 / 100)
parcelado = preco + (preco * 10 / 100)
print('O produto que custa R${:.2f}, passará a custar \nR${:.2f} - Avista com 10% de desconto. \nR${:.2f} - Parcelado com 10% de juros.'.format(preco, avista, parcelado))