#Faça um programa que leia um ano qualquer e
# mostre se ele é bissexto.

from datetime import date
ano = int(input('Qual ano você quer analisar? Ou digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year #irar pegar o ano atual configurado na maquina.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {}, é BISSEXTO.'.format(ano))
else:
    print('O ano {}, NÃO é BISSEXTO.'.format(ano))