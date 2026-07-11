print('''Exercício Python 105: Faça um programa que tenha uma função notas() que pode
 receber várias notas de alunos e vai retornar um dicionário com as seguintes
 informações:
– Quantidade de notas.
– A maior nota.
– A menor nota.
– A média da turma.
– A situação (opcional)
''')
print('-=' * 20)

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de uma turma.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação da turma.
    :return: dicionário com várias informações sobre a situação da turma.
    """

    turma = dict()
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['media'] = sum(n) / len(n)
    if sit:
        if turma['media'] >= 7:
            turma['situação'] = 'BOA'
        elif turma['media'] >= 5:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'RUIM'
    return turma


#Programa principal
resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
help(notas)