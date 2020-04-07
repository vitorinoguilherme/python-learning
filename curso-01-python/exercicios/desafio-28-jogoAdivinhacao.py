"""
 descobrindoNumero.py - Sorteia número entre 0-5 e indica se acertou o número.
 autor: Guilherme Vitorino
 04.04.20 - 21h17min
"""
from random import randint
from time import sleep

numeroComputador = randint(0, 5)

print('-=-' * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-=-' * 20)
numeroUsuario = int(input("Em que número pensei? "))

print("PROCESSANDO...")
sleep(1)
if numeroUsuario < 0 or numeroUsuario > 5:
    print("Digite um número entre 0-5!")
elif numeroUsuario == numeroComputador:
    print("PARABÉNS! Você venceu!")
else:
    print(f"Você PERDEU! Eu pensei no número {numeroComputador} e não no {numeroUsuario}")

