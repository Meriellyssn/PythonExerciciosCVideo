print('''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba 
dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será 
um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo 
do fatorial.''')
print('-=' * 20)

# def fatorial(n, show=False):
#     """
#     -> Calcula o Fatorial de um número.
#     :param n: O número a ser calculado.
#     :param show: (opcional) Mostra ou não o cálculo.
#     :return: O valor do Fatorial de um número n.
#     """
#     fact = 1
#     for cont in range(n, 0, -1):
#         if show:
#             print(cont, end='')
#             if cont > 1:
#                 print(f' x ', end='')
#             else:
#                 print(f' = ', end='')
#         fact *= cont
#     return fact
#
#
# #Programa principal
# print(fatorial(5, True))

def fatorial(n, show=False):
    """
     -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não o cálculo.
    :return: O valor do Fatorial de um número n.
    """
    fact = 1
    cont = n

    if show:
        print(f'Calculando o {n}! = ', end='')
    while cont > 0:
        if show:
            print(f'{cont}', end='')
            print(' x ' if cont > 1 else ' = ', end='')
        fact *= cont
        cont -= 1
    return fact

#Programa principal
num = int(input('Digite um número para calcular o fatorial: '))
print((fatorial(num, True)))