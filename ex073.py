print('-=-'*20)
print('''Crie uma tupla preenchida com os 20 primeiros colocados
 da Tabela do Campeonato Brasileiro de Futebol,
 na ordem de colocação. Depois mostre:
 a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.''')
print('-=-'*20)
time = ('Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo',
        'Atletico-PR', 'Bahia', 'Coritiba', 'EC Vitória',
        'Bragantino', 'Botafogo', 'Vasco da Gama', 'Grêmio',
        'Cruzeiro', 'Corinthians', 'Santos', 'Atletico-MG',
        'Internacional', 'Remo', 'Mirassol', 'Chapecoense')
print('-=-'*20)
print(f'Lista de time do Brasileirão: {time}')
print('-=-'*20)
#a) Os 5 primeiros times.
print(f'Os 5 primeiros são: {time[0:5]}')
print('-=-'*20)
#b) Os últimos 4 colocados.
print(f'Os 4 últimos colocados: {time[-4:]}')
print('-=-'*20)
#c) Times em ordem alfabética.
print(f'Os times em ordem alfabetica são: {sorted(time)}')
print('-=-'*20)
#d) Em que posição está o time da Chapecoense.
print(f'O Chapecoense está na {time.index("Chapecoense")+1}ª posição.')