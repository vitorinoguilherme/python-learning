'''
 porcaoInteira.py - Dado um número real exibe a porção inteira.
 autor: Guilherme Vitorino
 02.04.20 - 15h33min
'''

from math import trunc

number = float(input("Informe o número: "))

print(f"\nO número {number} tem a parte inteira {trunc(number)}.")

