print('Gerador de PA 3.0')
print('-=' * 20)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10 #Programa começa mostrando 10 termos.
while mais != 0:
    total += mais
    while contador <= total:
        print('{}'.format(termo), end=' -> ')
        termo += razao
        contador += 1
    print('PAUSA')
    print('-=' * 20)
    mais = int(input('Quantos termos a mais você deseja? '))
print('Progressão finalizada com {} termos exibidos.'.format(total))

