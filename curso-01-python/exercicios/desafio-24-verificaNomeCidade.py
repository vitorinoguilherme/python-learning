'''
 verificaNomeCidade.py - Dado a cidade verefica se o nome começa com 'SANTO'
 autor: Guilherme Vitorino
 04.04.20 - 17h27min
'''

cidade = input("Digite o nome da cidade: ")

divNomeCidade = cidade.split()          # Divide nomes da cidade

if 'SANTO' in divNomeCidade[0].upper():
    print(f"\nSim, o nome da cidade \"{cidade}\" "
          f"começa com \"{divNomeCidade[0].upper()}\"")
else:
    print(f"\nNão, o nome da cidade \"{cidade}\" "
          f"não começa com \"SANTO\"")