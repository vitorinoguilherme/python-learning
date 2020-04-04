"""
 firstAndLastName.py - Dado o nome completo mostra primeiro e ultimo nome.
 autor: Guilherme Vitorino
 04.04.20 - 18h15min
"""

nome = input("Digite o nome completo: ")

divNome = nome.split()
print(f"Primeiro Nome: {divNome[0]}\n"
      f"Último Nome: {divNome[-1]}")
