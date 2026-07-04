print('''Exercício Python 096: Faça um programa 
que tenha uma função chamada área(), que receba 
as dimensões de um terreno retangular (largura e
comprimento) e mostre a área do terreno.''')
print('-=' * 20)

def area():
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m².')

#Programa principal
print(' ' * 8,'Controle de Terrenos', ' ' * 8)
print('-=' * 20)
area()
