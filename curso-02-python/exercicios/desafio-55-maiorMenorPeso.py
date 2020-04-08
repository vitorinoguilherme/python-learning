"""
 maiorMenorPeso.py - Informa o maior e menor peso digitados.
 autor: Guilherme Vitorino
 08.04.20 - 14h45min
"""

lista = []
for num in range(0, 5):
    peso = float(input(f"Informe o peso da {num+1}º pessoa: (kg) "))
    lista.append(peso)

lista.sort()
print(f"Maior peso foi: \033[1;32m{lista[-1]}(kg) \033[m\n"
      f"Menor peso foi: \033[1;32m{lista[0]}(kg) \033[m")