'''
 comprimentoHipotenusa.py - Dados os catetos calcula a hipotenusa.
 autor: Guilherme Vitorino
 02.04.20 - 15h40min
'''

from math import pow, sqrt

catetoOposto = float(input("Informe o comprimento do cateto oposto: "))
catetoAdjacente = float(input("Informe o comprimento do cateto adjacente: "))

hipotenusa = sqrt((pow(catetoOposto, 2)+pow(catetoAdjacente,2)))

print(f"A hipotenusa = {hipotenusa:.2f}")
