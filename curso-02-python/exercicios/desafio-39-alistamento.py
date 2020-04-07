"""
 alistamento.py - Informa sobre o alistamento de acordo com a idade.
 autor: Guilherme Vitorino
 07.04.20 - 19h42min
"""
from datetime import date

anoNascimento = int(input("Informe o ano de nascimento: "))
idade = date.today().year - anoNascimento

print(f"Atualmente você tem {idade} anos.")

if idade < 18:
    print(f"Você ainda vai se alistar, faltam {(18-idade)} anos. ")
elif idade == 18:
    print("Esta na hora de se alistar! Você tem 18 anos. ")
elif idade > 18:
    print(f"Passou o tempo do alistamento. Você está {idade-18} anos atrasado.")

