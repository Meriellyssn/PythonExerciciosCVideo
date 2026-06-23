print('''Faça um programa que jogue par ou ímpar 
com o computador. O jogo só será interrompido 
quando o jogador perder, mostrando o total de 
vitórias consecutivas que ele conquistou no 
final do jogo.''')
print('-='*20)

from random import randint
vitorias = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo =  ' '
    #Fazendo a verificação se o usuário digitou par ou impar.
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total foi de {total}')
    print('Deu >> PAR' if total % 2 == 0 else 'Deu >> ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print('-='*20)
print(f'GAME OVER! Você venceu {vitorias} vezes')
print('-='*20)