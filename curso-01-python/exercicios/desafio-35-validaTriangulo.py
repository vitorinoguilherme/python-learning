"""
 validaTriangulo.py - Valida se os valores informados podem ou não formar um triângulo.
 autor: Guilherme Vitorino
 04.04.20 - 22h23min
"""
print("-=" * 20)
print("Informe os valores das segmentos ")
print("-=" * 20)

array = []
for i in range(3):
    retas = float(input(f" {i+1}º semento: "))
    array.append(retas)

if array[0] < array[1] + array[2] and array[1] < array[0] + array[2] and array[2] < array[0] + array[1]:
    print("Os segmentos podem formar um triângulo.")
else:
    print("Os segmentos não podem formar um triângulo.")