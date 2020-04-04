"""
 infoInputTeclado.py - Faz uma análise da frase digitada.
 autor: Guilherme Vitorino
 04.04.20 - 17h59min
"""

frase = input("Digite uma frase: ").strip()

print(f"\nNúmero de vezes que aparece letra \"A\": {frase.upper().count('A')}"
      f"\nPosição que aparece primeira vez: {frase.upper().find('A')+1}"
      f"\nPosição que aparece última vez: {frase.upper().rfind('A')+1}")
