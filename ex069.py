print(''''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer 
ou não continuar. No final, mostre: 
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.''')
print('-=' * 20)
print('{:^40}'.format('CADASTRO DE PESSOAS'))
print('-=' * 20)
tot18 = totH = totM20 = 0
while True:
    #1º Entrada de dados
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF': #1º Validação
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    #Processamento de Dados
    if idade >= 18:
        tot18 += 1
    if sexo =='M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    # 2º Entrada de dados
    resp = ' '
    while resp not in 'SN': #2º Validação
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 20)
#Saída de Dados
print(f'O total de pessoas com mais de 18 anos foi >> {tot18}')
print(f'Temos >> {totH} homens cadastrados.')
print(f'O total de mulheres com menos de 20 anos é de >> {totM20}')