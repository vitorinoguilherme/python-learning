'''
 conversorTamanhos.py - Dado o valor em (m) converte em (cm) e (mm).
 autor: Guilherme Vitorino
 02.04.20 - 13h49min
'''

valor = float(input("Informe o valor: "))

print(f"{valor:.2f}(m) em centímetros = {valor * 100}(cm) \n"
      f"{valor:.2f}(m) em milímetros = {valor * 1000}(mm)")
