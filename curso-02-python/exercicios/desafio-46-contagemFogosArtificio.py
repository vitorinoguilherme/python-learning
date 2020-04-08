"""
 contagemFogosArtificio.py - Contagem para estouro fogos de artifício.
 autor: Guilherme Vitorino
 08.04.20 - 12h14min
"""
from time import sleep

print(f"{' Contagem regressiva, fogos de artifício! ':=^80}")

for segundos in range(10, -1, -1):
    print(f"\033[1;33m{segundos:^80} ")
    sleep(1)


