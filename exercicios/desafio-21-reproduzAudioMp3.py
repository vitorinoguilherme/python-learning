'''
 reproduzAudioMp3.py - Reproduz o áudio de um arquivo mp3.
 autor: Guilherme Vitorino
 02.04.20 - 17h53min
'''

import pygame

pygame.init()
pygame.mixer.music.load('') # inserir nomeMusica.mp3
pygame.mixer.music.play()
pygame.event.wait()