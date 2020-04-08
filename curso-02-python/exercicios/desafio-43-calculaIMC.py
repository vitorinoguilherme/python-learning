"""
 calculaIMC.py - Calcula IMC e informa status.
 autor: Guilherme Vitorino
 07.04.20 - 20h29min
"""
from math import pow

cores = {'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'magenta': '\033[1;35m'}
peso = float(input("Informe seu peso: (kg) "))
altura = float(input("Informe sua altura: (m) "))
imc = peso / pow(altura, 2)

print(f"Seu IMC é {imc:.1f}, ", end='')
if imc <= 18.5:
    print(f"{cores['vermelho']}Você está ABAIXO do peso.")
elif 18.5 < imc <= 25:
    print(f"{cores['verde']}Você tem o peso NORMAL.")
elif 25 < imc <= 30:
    print(f"{cores['magenta']}Você está com SOBREPESO.")
elif 30 < imc <= 40:
    print(f"{cores['vermelho']}Você está com OBESIDADE.")
elif imc > 40:
    print(f"{cores['vermelho']}Você está com OBESIDADE MÓRBIDA.")
