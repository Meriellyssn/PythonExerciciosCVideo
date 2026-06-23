#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
pygame.mixer.get_init()'''

import pygame, time

pygame.mixer.init(frequency=16000)
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(0.1)
