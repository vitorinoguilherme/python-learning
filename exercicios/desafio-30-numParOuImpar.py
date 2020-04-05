"""
 numParOuImpar.py - Informa se o número digitado é par ou ímpar
 autor: Guilherme Vitorino
 04.04.20 - 21h44min
"""

numero = int(input("Informe um número: "))

if numero % 2 == 0:
    print("Número é Par.")
else:
    print("Número é Impar.")