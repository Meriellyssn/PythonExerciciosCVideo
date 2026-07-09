print('''Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que 
receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O 
programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha 
sido informado corretamente.''')
print('-=' * 20)

def ficha(jog='<desconhecido>', gol=0):
    if jog.strip() == '':
        jog = '<desconhecido>'
    print(f'O jogador {jog}, fez {gol} gol(s) no campeonato.')


#Programa principal
n = str(input('Nome do jogador: ')).upper()
g = str(input('Números de gol(s): '))
g = int(g) if g.isnumeric() else 0
ficha(n, g)
print('-=' * 20)