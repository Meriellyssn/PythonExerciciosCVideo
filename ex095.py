jogador = dict()
partidas = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().upper()
    total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for part in range(total_partidas):
        partidas.append(int(input(f' - Quantos gols na partida {part + 1}: ')))

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'S':
            break
        print('Erro! Digite apenas S ou N.')
        if resp == 'N':
            break
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