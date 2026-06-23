#Faça um programa que leia o ano de nascimento
# de um jovem e informe, de acordo com a sua
# idade, se ele ainda vai se alistar ao serviço
# militar, se é a hora exata de se alistar ou
# se já passou do tempo do alistamento. Seu
# programa também deverá mostrar o tempo que
# falta ou que passou do prazo.

from datetime import date
atual = date.today().year
print('Analise de Alistamento')
print('-=' * 10)
nasc = int(input('Ano de nascimento: '))
sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if sexo == 'M':
    if idade == 18:
        print('Você precisa se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda falta(m) {} ano(s) para o seu alistamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} ano(s).'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
else:
   print("O alistamento para você não é OBRIGATÓRIO!")