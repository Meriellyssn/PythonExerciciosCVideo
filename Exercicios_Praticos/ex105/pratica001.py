
def analisar_lotes(*n, status=False):
    """
    -> Função que analisa a quantidade de linhas de arquivos CSV.
    :param n: Um ou vários arquivos CSV.
    :param status: Valor opcional, indicando a situação do processamento.
    :return: Dicionário com várias informações sobre os lotes analisados
    (total, maior, menor, media e situação).
    """

    lotes = dict()
    lotes['total'] = len(n)
    lotes['maior'] = max(n)
    lotes['menor'] = min(n)
    lotes['media'] = sum(n) /len(n)
    if status:
        if lotes['media'] > 1000:
            lotes['status'] = 'Processamento Pesado!'
        else:
            lotes['status'] = 'Processamento Leve!'

    return lotes

# ==========================================
#        PROGRAMA PRINCIPAL DE TESTES
# ==========================================

# 1. Testando a sua Docstring (Manual Interativo)
print('-=' * 30)
print(' 📖 LENDO O MANUAL DA FUNÇÃO ')
print('-=' * 30)
help(analisar_lotes)

# 2. Testando a função SEM o parâmetro status (modo padrão)
print('\n' + '-=' * 30)
print(' 🧪 TESTE 1: Sem o status ativado ')
print('-=' * 30)
resultado_padrao = analisar_lotes(250, 400, 150, 900)
print(resultado_padrao)

# 3. Testando a função COM o parâmetro status ativado (Cenário Leve)
print('\n' + '-=' * 30)
print(' 🧪 TESTE 2: Com status (Cenário: Processamento Leve) ')
print('-=' * 30)
resultado_leve = analisar_lotes(500, 800, 100, status=True)
print(resultado_leve)

# 4. Testando a função COM o parâmetro status ativado (Cenário Pesado)
print('\n' + '-=' * 30)
print(' 🧪 TESTE 3: Com status (Cenário: Processamento Pesado) ')
print('-=' * 30)
resultado_pesado = analisar_lotes(1500, 3200, 800, 4500, status=True)
print(resultado_pesado)