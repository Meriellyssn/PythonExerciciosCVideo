print('''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média''')

'''
Informações:
1: leia nome, sexo e idade de várias pessoas, e perguntar de quer continuar.

'''

galera = list()
soma = 0

while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: ')).strip().upper()
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        print('Erro!: Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    galera.append(pessoa.copy())

    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        print('Erro: Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

media = soma / len(galera)

print('-=' * 20)
#A) Quantas pessoas foram cadastradas.
print(f'- Ao todo temos {len(galera)} pessoa(s) cadastrada(s).')
#B) A média de idade.
print(f'- A média de idade é de {media:.0f} anos.')
#C) Uma lista com as mulheres.
print(f'- As mulher(es) cadastrada(s) foram:', end='')
for pessoa in galera:
    if pessoa['sexo'] == 'F':
        print(f'[{pessoa["nome"]}] ', end='')
print()
#D) Uma lista de pessoas com idade acima da média
print('- Lista de pessoas que estão acima da média:')
for pessoa in galera:
    if pessoa['idade'] > media:
        print(f'  Nome = {pessoa["nome"]}; sexo = {pessoa["sexo"]}; idade = {pessoa["idade"]};')
    else:
        print('  Sem média')
print('-=' * 3, 'Fim do Programa', '-=' * 3)