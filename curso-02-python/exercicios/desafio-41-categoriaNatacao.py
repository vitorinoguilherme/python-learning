"""
 categoriaNatacao.py - De acordo com a idade mostra a classificação do atleta.
 autor: Guilherme Vitorino
 07.04.20 - 20h15min
"""

from datetime import date

anoNascimento = int(input("Informe o ano de nascimento: "))
idade = date.today().year - anoNascimento

if idade <= 9:
    print(f"Você tem {idade} anos, Sua categoria de natação é \033[1;32mMIRIM!")
elif 9 < idade <= 14:
    print(f"Você tem {idade} anos, Sua categoria de natação é \033[1;32mINFANTIL!")
elif 14 < idade <= 19:
    print(f"Você tem {idade} anos, Sua categoria de natação é \033[1;32mJUNIOR!")
elif 19 < idade <= 20:
    print(f"Você tem {idade} anos, Sua categoria de natação é \033[1;32mSÊNIOR!")
else:
    print(f"Você tem {idade} anos, Sua categoria de natação é \033[1;32mMASTER!")