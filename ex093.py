print('''Crie um programa que gerencie o aproveitamento de um jogador de 
futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso 
será guardado em um dicionário, incluindo o total de gols feitos durante o 
campeonato.''')
print('-=' * 20)

jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: ')).strip()
total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for cont in range(total_partidas):
    partidas.append(int(input(f'Quantos gols na partida {cont +1}: ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=' * 20)
print(jogador)
print('-=' * 20)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor: {valor}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for chave, valor in enumerate(partidas):
    print(f'Na partida {chave + 1}, fez {valor} gols.')