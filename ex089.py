ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 20)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 40)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-' * 40)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        print('FINALIZANDO...')
        break
    if opcao <= len(ficha) -1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print('>>> VOLTE SEMPRE <<<')