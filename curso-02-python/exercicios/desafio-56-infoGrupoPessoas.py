"""
 infoGrupoPessoas.py - Informações sobre um grupo de pessoas
 autor: Guilherme Vitorino
 08.04.20 - 14h55min
"""
somaIdades = 0
maiorIdade = 0
contadorMulheres = 0
listaPessoas = []

for num in range(0, 4):
    nome = str(input("Digite o seu nome: ")).strip().capitalize()
    listaPessoas.append(nome)

    idade = int(input("Digite sua idade: "))
    listaPessoas.append(idade)
    somaIdades += idade

    sexo = str(input("Informe seu sexo ['MASCULINO' == 'M','FEMININO' == 'F','OUTRO' == 'O']: ")).strip().upper()
    listaPessoas.append(sexo)

    if maiorIdade < idade and sexo == 'M' or sexo == 'MASCULINO':
        maiorIdade = idade
        homemMaisVelho = nome
    if sexo == 'FEMININO' or sexo == 'F' and idade < 20:
        contadorMulheres += 1

print(f"""\033[1mA média de idade do grupo é: {(somaIdades/4):.1f} anos.
O nome do homem mais velho é {homemMaisVelho} ele tem {maiorIdade} anos.
{contadorMulheres} mulher(es) tem menos de 20 anos.
""")

