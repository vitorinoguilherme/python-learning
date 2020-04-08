"""
 jokenpo.py - Jogo do jokenpo vs computador.
 autor: Guilherme Vitorino
 07.04.20 - 21h08min
"""
from time import sleep
from random import randint

cores = {'limpa': '\033[m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'magenta': '\033[1;35m',
         'azul': '\033[1;34m', 'amarelo':'\033[33m'}

print(f"{cores['azul']}-=" * 20)
print("Vamos jogar, Jokenpo!")

jogadas = ['pedra', 'papel', 'tesoura']

print(f"Prepare-se: \n"
      f"1 - PEDRA \n"
      f"2 - PAPEL \n"
      f"3 - TESOURA")
jogador = jogadas[int(input(f"Escolha sua jogada ->")) - 1]
computador = jogadas[randint(0,2)]

print(f"-=" * 20)

print(f"{cores['limpa']}{cores['verde']}Vamos lá estou pronto. \nProcessando...")
sleep(1.7)

if jogador == 'pedra' and computador == 'tesoura':
    print(f"Parabéns você GANHOU, escolheu {jogador} e eu {computador}")
elif jogador == 'papel' and computador == 'pedra':
    print(f"Parabéns você GANHOU, escolheu {jogador} e eu {computador}")
elif jogador == 'tesoura' and computador == 'papel':
    print(f"Parabéns você GANHOU, escolheu {jogador} e eu {computador}")
elif jogador == computador:
    print(f"{cores['amarelo']}Parece que EMPATAMOS =/, escolheu {jogador} e eu {computador}")
else:
    print(f"{cores['vermelho']}Você PERDEU '-', escolheu {jogador} e eu {computador}")

