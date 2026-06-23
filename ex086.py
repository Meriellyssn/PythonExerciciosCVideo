print('''Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.''')

# Inicialização de uma matriz 3x3 preenchida com zeros.
# Cada sublista representa uma linha da matriz.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# ==============================================================================
# 1. BLOCO DE LEITURA (ENTRADA DE DADOS)
# ==============================================================================
# O primeiro loop controla as linhas (de 0 a 2)
for linha in range(0, 3):
    # O segundo loop controla as colunas (de 0 a 2) para a linha atual
    for coluna in range(0, 3):
        # Solicita o valor ao usuário, converte para inteiro e armazena na posição exata [linha][coluna]
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 20)

# ==============================================================================
# 2. BLOCO DE EXIBIÇÃO (SAÍDA DE DADOS FORMATADA)
# ==============================================================================
# Percorre novamente as linhas da matriz
for linha in range(0, 3):
    # Percorre as colunas da linha atual
    for coluna in range(0, 3):
        # Exibe o valor da matriz com formatação especial:
        # :^5  -> Centraliza o número em um espaço de 5 caracteres.
        # end='' -> Evita a quebra de linha automática do print, mantendo os elementos na mesma linha.
        print(f'[{matriz[linha][coluna]:^5}]', end='')

    # Após imprimir todos os elementos de uma coluna (uma linha completa),
    # este print vazio força a quebra de linha para começar a próxima linha da matriz.
    print()

# Fecha a exibição com outra linha divisória visual
print('-=' * 20)