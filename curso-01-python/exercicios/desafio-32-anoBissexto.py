"""
 anoBissexto.py - Informa se o ano é bissexto ou não.
 autor: Guilherme Vitorino
 04.04.20 - 21h58min
"""
from datetime import date

ano = int(input("Informe o ano (0 para analisar ano atual): "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é Bissexto.")
else:
    print(f"O ano {ano} não é Bissexto.")