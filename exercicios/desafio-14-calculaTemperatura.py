'''
 calculaTemperatura.py - Dado a temperatura em 'C transforma em 'F.
 autor: Guilherme Vitorino
 02.04.20 - 14h06min
'''

grauC = float(input("Informe a temperatura em 'C: "))
grauF = ((9 * grauC) / 5) + 32

print(f"A temperatura de {grauC}'C\n"
      f"Corresponde a {grauF}'F")