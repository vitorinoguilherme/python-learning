"""
 descobrindoNumero.py - Sorteia número entre 0-5 e indica se acertou o número.
 autor: Guilherme Vitorino
 04.04.20 - 21h17min
"""
from random import randint

numeroComputador = randint(0, 5)

numeroUsuario = int(input("Tente descobrir qual foi o número escolhido pelo computador (0-5): "))

if numeroUsuario < 0 or numeroUsuario > 5:
    print("Digite um número entre 0-5!")
elif numeroUsuario == numeroComputador:
    print("Parabéns você venceu.")
else:
    print("Você perdeu. Tente novamente.")

