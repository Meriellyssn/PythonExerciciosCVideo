real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.23
euro = real / 6.08
print('Com R${:.2f} você pode comprar \n>>> US${:.2f} \n>>> EUR${:.2f}'.format(real, dolar, euro))