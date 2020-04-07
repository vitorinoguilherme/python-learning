'''
 angulosSenCosTan.py - Dado o ângulo cálcula seno, cosseno e tangente.
 autor: Guilherme Vitorino
 02.04.20 - 15h48min
'''

from math import sin, cos, tan, radians

angulo = float(input("Digite o ângulo: "))
angulo = radians(angulo)

print(f"Ângulo informado: {angulo:3.2f}\n"
      f"Seno: {sin(angulo):.2f}\n"
      f"Cosseno: {cos(angulo):.2f}\n"
      f"Tangente: {tan(angulo):.2f}")
