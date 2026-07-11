print('''📋 Enunciado do Desafio: Você é um Engenheiro de Dados criando um script de auditoria para um Data Lake. 
Crie um programa com uma função chamada auditar_lotes() que receba uma quantidade variável de números inteiros 
representando a quantidade de registros (linhas) processados em diferentes arquivos CSV ao longo do dia. O seu 
programa deve analisar esses valores, exibir um por um na tela, informar quantos arquivos foram processados ao todo e
qual foi o maior lote recebido. Realize testes passando 5 valores, 3 valores e nenhum valor para validar a 
função.''')
from time import sleep

def auditar_lotes(* registros):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os registros passados...')
    for lote in registros:
        print(f'[{lote}] ', end='', flush=True)
        sleep(0.5)

        if cont == 0:
            maior = lote
        else:
            if lote > maior:
                maior = lote
        cont += 1
    print()
    print(f'Foram informados {cont} registros.', flush=True)
    sleep(0.5)
    print(f'O maior registro informado foi [{maior}].', flush=True)
    sleep(0.5)


#Programa Principal
auditar_lotes(10, 32, 15, 58, 106)
auditar_lotes(150, 369, 741)
auditar_lotes()