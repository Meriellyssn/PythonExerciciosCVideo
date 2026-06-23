"""Enunciado do Desafio: Imagine que você foi chamado para programar o sistema de triagem de um grande evento de tecnologia. Os convidados recebem crachás com números de identificação (IDs). Para evitar filas na entrada, a organização criou uma regra: IDs com numeração PAR devem ser direcionados para a lista do "Portão A", e IDs com numeração ÍMPAR devem ir para a lista do "Portão B".
Crie um programa em Python que leia o ID numérico de vários convidados continuamente. O programa deve guardar todos em uma lista geral primeiro. Depois, o sistema deve analisar essa lista principal e distribuir os números para as duas listas específicas (Portão A e Portão B). No final, exiba as três listas formatadas.
"""

ids = []
portao_A = []
portao_B = []
while True:
    ids.append(int(input('Digite o ID de Identificação: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
for num in ids:
    if num % 2 == 0:
        portao_A.append(num)
    elif num % 2 == 1:
        portao_B.append(num)
print('-=' * 20)
print(f'Os IDs cadastrados foram: {ids}')
portao_A.sort()
print(f'Os IDs do Portão A são: {portao_A}')
portao_B.sort()
print(f'Os IDs do Portão B são: {portao_B}')

