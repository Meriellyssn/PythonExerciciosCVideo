
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().upper()
    total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    partidas.clear()
    for part in range(total_partidas):
        partidas.append(int(input(f' - Quantos gols na partida {part + 1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if resp == 'N':
        break


print('-=' * 20)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('--' * 20)
for chave, valor in enumerate(time):
    print(f'{chave:>3} ', end='')
    for dado in valor.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-=' * 20)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 encerra...): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR >> {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'  No jogo {i + 1}, fez {g} gols.')
    print('-=' * 20)
print('--- Volte Sempre ---')