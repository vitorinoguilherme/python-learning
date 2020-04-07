"""
 calculaIMC.py - Calcula IMC e informa status.
 autor: Guilherme Vitorino
 07.04.20 - 20h29min
"""
from math import pow

cores = {'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'magenta': '\033[1;35m'}
peso = float(input("Informe seu peso: kg "))
altura = float(input("Informe sua altura: m "))
imc = peso / pow(altura, 2)

if imc <= 18.5:
    print(f"Seu IMC é {imc:.2f}, {cores['vermelho']}Você está abaixo do peso.")
elif 18.5 < imc <= 25:
    print(f"Seu IMC é {imc:.2f}, {cores['verde']}Você tem o peso ideal.")
elif 25 < imc <= 30:
    print(f"Seu IMC é {imc:.2f}, {cores['magenta']}Você está com sobrepeso.")
elif 30 < imc <= 40:
    print(f"Seu IMC é {imc:.2f}, {cores['vermelho']}Você com obesidade.")
elif imc > 40:
    print(f"Seu IMC é {imc:.2f}, {cores['vermelho']}Você está com obesidade mórbida.")
