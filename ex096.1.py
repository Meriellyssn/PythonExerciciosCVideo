#Exemplo como o professor resolveu.
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


#Programa principal
print(' ' * 8,'Controle de Terrenos', ' ' * 8)
print('-=' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
