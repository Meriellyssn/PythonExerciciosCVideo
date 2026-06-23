print('''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.''')
print('-' * 20)
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMAR', 'FUTURO')
for p in palavras:
    print(f'\nNa palavra {p} temos >', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
