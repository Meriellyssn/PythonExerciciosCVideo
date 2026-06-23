"""📋 Enunciado do Desafio: Você foi contratado como Desenvolvedor Júnior em uma grande plataforma de ensino à distância (EAD). Os professores cadastram diariamente centenas de fórmulas matemáticas complexas no banco de dados para gerar as provas dos alunos. O problema é que, às vezes, um professor digita rápido demais e esquece de fechar um parêntese, quebrando o sistema do aluno.
A sua missão é criar o "Filtro de Qualidade" do sistema. Crie um programa em Python que receba a fórmula digitada pelo professor e, utilizando a lógica de "Pilha", analise se todos os parênteses abertos ( possuem um correspondente fechando ) na ordem correta
. No fim, exiba uma mensagem aprovando a entrada no banco de dados ou rejeitando a fórmula por erro de sintaxe."""

formula = str(input('Digite a fórmula: '))
pilha = []
for simbolo in formula:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Fórmula Valida!')
else:
    print('Fórmula Inválida! Tente novamente.')
print('-=' * 20)
