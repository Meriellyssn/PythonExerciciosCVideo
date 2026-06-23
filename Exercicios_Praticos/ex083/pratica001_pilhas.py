expr = str(input('Digite uma expressão: '))
pilha = []
for simbolo in expr:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
         if len(pilha) > 0:
            pilha.pop()
         else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão Valida!')
else:
    print('Expressão Inválida! Tente novamente.')