'''
 informacoesNome.py - Dado nome completo faz transformações.
 autor: Guilherme Vitorino
 04.04.20 - 16h53min
'''

nome = input("Digite o nome completo: \n")

print(f"Nome com letras Maiúsculas: {nome.upper()}")
print(f"Nome com letras Minúsculas: {nome.lower()}")

divisaoNome = nome.strip()          # Remove espaços antes e depois
divisaoNome = divisaoNome.split()   # Divide a String nos espaços
divisaoNome = ''.join(divisaoNome)  # Junta a String sem espaços
print(f"Nome sem considerar espaços: {len(divisaoNome)}")

primeiroNome = nome.strip().split()
print(f"Quantidade letras Primeiro Nome: {len(primeiroNome[0])}")