"""
 validaTrianguloAprimorado.py - Valida se os valores informados podem ou não formar um triângulo.
 autor: Guilherme Vitorino
 07.04.20 - 20h24min
"""
print("-=" * 20)
print("Informe os valores das segmentos ")
print("-=" * 20)

array = []
for i in range(3):
    retas = float(input(f" {i+1}º segmento: "))
    array.append(retas)

if array[0] < array[1] + array[2] and array[1] < array[0] + array[2] and array[2] < array[0] + array[1]:
    print("Os segmentos acima podem formar um triângulo", end=' ')
    if array[0] == array[1] == array[2]:
        print(f"\033[1;32mEQUILÁTERO!")
    elif array[0] != array[1] != array[2] != array[0]:
        print(f"\033[1;32mESCALENO!")
    else:
        print(f"\033[1;32mISÓSCELES!")
else:
    print("Os segmentos não podem formar um triângulo.")

