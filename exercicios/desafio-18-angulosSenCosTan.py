'''
 angulosSenCosTan.py - Dado o ângulo cálcula seno, cosseno e tangente.
 autor: Guilherme Vitorino
 02.04.20 - 15h48min
'''

from math import sin, cos, tan

angulo = float(input("Digite o ângulo: "))

print(f"Ângulo informado: {angulo:3.2f}\n"
      f"Seno: {sin(angulo)}\n"
      f"Cosseno: {cos(angulo)}\n"
      f"Tangente: {tan(angulo)}")
