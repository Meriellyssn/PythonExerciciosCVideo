print('''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.''')

#usando "for".
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #transformando a frase em uma lista.
junto = ''.join(palavras) #Transformando a lista em uma unica strig.
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO é um PALÍNDROMO!')

print('-=' * 20)

#Usando fatiamento.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #transformando a frase em uma lista.
junto = ''.join(palavras) #Transformando a lista em uma unica strig.
inverso = junto[:: -1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO é um PALÍNDROMO!')

print('-=' * 20)