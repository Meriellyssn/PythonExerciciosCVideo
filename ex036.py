#Escreva um programa para aprovar o empréstimo
# bancário para a compra de uma casa. Pergunte o
# valor da casa, o salário do comprador e em
# quantos anos ele vai pagar. A prestação mensal
# não pode exceder 30% do salário ou então o
# empréstimo será negado.

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100 #regra de negócio, 'não pode passar de 30% do salário do comprador'
print('Para pagar uma casa de R${:.2f} em {} anos,'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}.'.format(prestacao))
if prestacao <= minimo:
    print('\033[32mEmpréstimo pode ser APROVADO!\033[m')
else:
    print('\033[31mEmpréstimo NEGADO!\033[m')
