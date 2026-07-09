print('''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt
‘Digite um n: ‘)''')
print('-=' * 20)

def leia_int(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


#Programa principal
n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')