print('''Crie um programa que gerencie o aproveitamento de um jogador de 
futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso 
será guardado em um dicionário, incluindo o total de gols feitos durante o 
campeonato.''')
#Estraindo Informações:
'''1 etapa: ler o nome do jogador e quantas partidas ele jogou.--- OK
etapa 2: ler a quantidade de gols feitos em cada partida. -- OK
3: guardar todos os dados em um dicionário. -- OK
4:incluindo o total de gols. -- OK
'''

print('-=' * 20)

jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: ')).strip().upper()
total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for part in range(total_partidas):
    partidas.append(int(input(f' - Quantos gols na partida {part + 1}: ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=' * 20)
print(jogador)
print('-=' * 20)
for chave, valor in jogador.items():
    print(f'O {chave} tem o valor: {valor}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {len(partidas)} partidas.')
for chave, valor in enumerate(partidas):
    print(f'  => Na partida {chave + 1}, fez {valor} gols.')
print(f'Foi um total de {jogador["total"]} gols.')