print('''Crie um programa que leia nome, ano de 
nascimento e carteira de trabalho e cadastre-o (com 
idade) em um dicionário. Se por acaso a CTPS for 
diferente de ZERO, o dicionário receberá também o ano de 
contratação e o salário. Calcule e acrescente, além da 
idade, com quantos anos a pessoa vai se aposentar.''')
print('-=' * 20)

from datetime import date
dados = dict()

dados['nome'] = str(input('Nome: ')).strip()
ano_nasc = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - ano_nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano da contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = (35 + dados['contratação']) - ano_nasc

print('-=' * 20)
for chave, valor in dados.items():
    print(f'- {chave.capitalize()} tem o valor: {valor}')