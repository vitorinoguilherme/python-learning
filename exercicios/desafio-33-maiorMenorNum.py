"""
 maiorMenorNum.py - Indica o menor e maior número digitados.
 autor: Guilherme Vitorino
 04.04.20 - 22h04min
"""
array = []

for i in range(3):
    numero = float(input("Informe um número: "))
    array.append(numero)

array.sort()
print(f"Menor número: {array[0]:.2f}\n"
      f"Maior número: {array[-1]:.2f}")