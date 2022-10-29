from nave import *
import pathlib
import csv

actual_path = pathlib.Path(__file__).parent.absolute()


with open('naves.csv', newline='') as f:
    reader = csv.reader(f)
    for naves in reader:
        print(naves)

def imprimirNaves():
    return print(naves)

def ordenar_nombres():
    nombres = [a.nombre, b.nombre, c.nombre, d.nombre, e.nombre]
    nombres.sort()
    print(nombres)
    nombres.reverse()
    print(nombres)


a = Nave("Estrella de la muerte", 500, 8998, 69420)
b = Nave("Halcon milenario", 1234, 1059, 1919191)
c = Nave("Lanzador imperial", 9999, 222, 37201)
d = Nave("Destructor estelar", 3721, 3939, 77777)
e = Nave("Supremacy", 56565, 12198, 66666)


if __name__ == "__main__":
        
    """"
    ordenar_nombres()
    """

    imprimirNaves()



