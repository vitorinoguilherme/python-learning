"""
 verificaNomePessoa.py - Dado o nome informa se contém ou não o nome 'SILVA'
 autor: Guilherme Vitorino
 04.04.20 - 17h50min
"""

nome = input("Digite seu nome completo: ")

if 'SILVA' in nome.upper():
    print(f"\nSim, o nome \"{nome}\" contém o nome \"SILVA\"")
else:
    print(f"\nNão, o nome \"{nome}\" não contém o nome \"SILVA\"")