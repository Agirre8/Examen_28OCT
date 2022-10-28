

#Funcion que hace los calculos de la regla se Sarrus
lista = []
def determinanteSarrus(self):
    for l in range(1, 4):
        for c in range(1, 4):
            matriz = int(input(f"[Inserte un valor [{l}, {c}] "))
            lista.append(matriz)
    primero = (lista[0] * lista[4] * lista[8])
    segundo = (lista[1] * lista[5] * lista[6])
    tercero = (lista[2] * lista[3] * lista[7])
    primero2 = (lista[2] * lista[4] * lista[6])
    segundo2 = (lista[0] * lista[5] * lista[7])
    tercero2 = (lista[1] * lista[3] * lista[8])

    sum = ((primero + segundo + tercero) - (primero2 + segundo2 + tercero2))


print(f"[El resultado es =[m")
for c in range(len(lista)):
    print(f"[{lista[c] }]",end='\n' if c == 2 or c == 5 else "")
print(f'\n[1;34mdet(a) = [1;35m{determinanteSarrus.sum}',end='')