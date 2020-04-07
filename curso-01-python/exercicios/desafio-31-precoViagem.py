"""
 precoViagem.py - Calcula preço da passagem de acordo com a distância.
 autor: Guilherme Vitorino
 04.04.20 - 21h50min
"""
distancia = float(input("Informe a distância: Km "))

if distancia <= 200.0:
    print(f"Valor da viagem: R$ {(0.50 * distancia):.2f}")
else:
    print(f"Valor da viagem: R$ {(0.45 * distancia):.2f}")
