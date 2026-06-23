#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()# já elimina os espaços no inicio e no fim da frase
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é >>> {}.'.format(nome.upper()))
print('Seu nome em letras minusculas é >>> {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))#elimina os espaços no meio das palavras

#1 opção
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))#identifica a quantidade de letras do primeiro nome

#opção 2
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))