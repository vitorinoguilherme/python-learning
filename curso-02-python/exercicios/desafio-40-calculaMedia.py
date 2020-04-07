"""
 calculaMedia.py - Dados duas notas calcula media e informa situação do aluno.
 autor: Guilherme Vitorino
 07.04.20 - 20h02min
"""
from time import sleep

print("-=" * 20)
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2
print("-=" * 20)

print("\033[1;32mProcessando...")
sleep(1.5)


if media < 5.0:
    print(f"\033[1;31mREPROVADO com media {media}")
if 5.0 <= media <= 6.9:
    print(f"\033[1;34mRECUPERAÇÃO com media {media}")
elif media >= 7.0:
    print(f"\033[1;32mAPROVADO com media {media}")
