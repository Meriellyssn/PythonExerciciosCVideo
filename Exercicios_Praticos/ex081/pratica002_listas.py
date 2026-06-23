"""🛠️ Desafio Mão na Massa Bônus: O Radar da Rodovia
📋 Enunciado do Desafio: Imagine que você foi contratado pela concessionária de uma rodovia para criar um pequeno sistema de auditoria de radares móveis. O seu programa em Python deve ler a velocidade de vários carros que passaram pelo radar e armazená-las em uma lista.
A cada velocidade registrada, o sistema deve perguntar se o operador deseja continuar inserindo novos carros.
Quando o turno acabar e o operador decidir parar, o sistema deve emitir um relatório automático mostrando:
Quantos veículos foram registrados pelo radar no total.
O "Ranking de Velocidade", exibindo a lista de todas as velocidades capturadas organizadas em ordem decrescente (do mais rápido para o mais lento).
Uma verificação de infração específica: O sistema deve checar se algum carro passou na velocidade exata de 100 km/h (uma velocidade acima do permitido) e exibir um alerta.
🚀 Requisitos/Critérios de Sucesso:
Utilizar uma lista vazia e o método .append() para incluir os dados dinamicamente.
Utilizar um laço while para ler dados até o usuário digitar "N".
Utilizar a função de leitura de comprimento para o total de carros.
Utilizar a ordenação com reversão de estado (ordem decrescente).
Utilizar o operador lógico simplificado para buscar o valor 100 na coleção."""

veiculos = list()
while True:
    veiculos.append(float(input('Digite a velocidade do veiculo: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja registar outro veiculo? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 20)
print(f'Foram registrados {len(veiculos)} veiculos hoje.')
veiculos.sort(reverse=True)
print(f'O Ranking de Velocidade: {veiculos}')
if 100 in veiculos:
    print('Infração Detectada: 100 km velocidade acima do permitido!')
else:
    print('Não foram encontrado velocidade acima do permitido: 100km')