print('''Exercício Python 097: Faça um programa 
que tenha uma função chamada escreva(), que 
receba um texto qualquer como parâmetro e mostre
 uma mensagem com tamanho adaptável.
 Ex:escreva(‘Olá, Mundo!’) 
 Saída:
 ~~~~~~~~~
 Olá, Mundo!
 ~~~~~~~~~
 ''')
print('-=' * 20)
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


#Programa Principal
escreva('Meirielly')
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')