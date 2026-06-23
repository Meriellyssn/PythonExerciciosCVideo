#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

#1 opção
import math
angulo = float(input('Digite o ângulo desejado: '))
seno = math.sin(math.radians(angulo))
co = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O ângulo de {}°, tem o: \n>>> SENO de {:.2f}. \n>>> COSSENO de {:.2f}. \n>>> TANGENTE de {:.2f}.'.format(angulo, seno, co, tan))

#2 opção
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo desejado: '))
seno = sin(radians(angulo))
co = cos(radians(angulo))
tan = tan(radians(angulo))
print('O ângulo de {}°, tem o: \n>>> SENO de {:.2f}. \n>>> COSSENO de {:.2f}. \n>>> TANGENTE de {:.2f}.'.format(angulo, seno, co, tan))
