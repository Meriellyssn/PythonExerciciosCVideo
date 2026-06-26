galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).strip().upper()

    while True: #Validação de sexo
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas F ou M.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True: #Validação de resposta
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 20)
print(f'- Foram cadastradas {len(galera)} pessoas.')
media = soma / len(galera)
print(f'- A média de idade é de {media:.0f} anos. ')
print(f'- A(s) Mulher(es) cadastrada(s) foram:', end='')
for pessoa in galera:
    if pessoa['sexo'] == 'F':
        print(f'[{pessoa["nome"]}]', end='')
print()
print('- A lista de pessoas que estão acima da média:', end='')
for pessoa in galera:
    if pessoa['idade'] > media:
        print(f'Nome: {pessoa["nome"]}; Sexo: {pessoa["sexo"]}; Idade: {pessoa["idade"]}')

print('-=' * 3, 'Fim do Programa', '-=' * 3)