print('''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.''')
print('-=' * 10)

from time import sleep
opcao = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('-=' * 10)
while opcao != 5:
    print('O que deseja fazer?')
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = int(input('Qual a opção desejada? '))
    print('-=' * 10)
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é igual a >> {}.'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('A multiplicação entre {} x {} é igual a >> {}.'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor entre {} e {} e >> {}.'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Digite novamente o primeiro valor: '))
        n2 = int(input('Digite novamente o segundo valor: '))
    elif opcao ==5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção Inválida! Tente novamente.')
    print('-=' * 10)
print('Fim do programa! Volte sempre...')