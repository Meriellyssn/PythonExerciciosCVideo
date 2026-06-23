"""- **📋 Enunciado do Desafio:** Crie um programa em Python que leia as notas de diversos alunos de uma turma e as armazene em uma lista. A cada nota inserida, o programa deve perguntar se você quer continuar ou não. Ao final do cadastro, o programa deve exibir três informações cruciais:
    1. Quantas notas foram digitadas no total.
    2. A lista de notas organizada em ordem decrescente (da maior para a menor nota).
    3. Uma mensagem informando se a nota **`5`** foi digitada e consta na lista.
- **🚀 Requisitos/Critérios de Sucesso:**
    - Criar um loop infinito ou de controle para a entrada contínua de dados.
    - Usar a função de medição correta para exibir o total de números da lista.
    - Aplicar o método de ordenação com o parâmetro de reversão.
    - Utilizar a condicional simplificada de busca sem usar repetições (**`in`**)."""

notas = []
while True:
    notas.append(float(input('Digite uma nota: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja registar outro veiculo? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 20)

print(f'Foram digitadas {len(notas)} notas.')
notas.sort(reverse = True)
print(f'As notas em ordem Decrescente são: {notas}')
if 5 in notas:
    print('A nota 5 consta na lista!')
else:
    print('A nota 5 NÃO consta na lista!')
