nome = str(input("Digite seu nome: ")).strip()

print(f'Olá, muito prazer em te conhecer\033[1;32m {nome}!! \033[m')

cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'}

print(f"{cores['azul']}Aprendizagem Python - Sistema de Cores {cores['limpa']}")



