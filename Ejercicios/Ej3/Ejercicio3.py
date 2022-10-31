from nave import *
import pathlib
import csv
import pandas
from collections import defaultdict

actual_path = pathlib.Path(__file__).parent.absolute()
with open('naves.csv', newline='') as f:
    reader = csv.reader(f)
    naves = list(reader)

def leerCSV_1():
    columns = defaultdict(list) # each value in each column is appended to a list

    with open('naves.csv') as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value 
                columns[k].append(v)

def imprimirNaves():
    return print(naves)

def ordenar_nombres():
    
    nombres = [a.nombre, b.nombre, c.nombre, d.nombre, e.nombre]
    nombres.sort()
    print(nombres)
    nombres.reverse()
    print(nombres)

def ordenar_nombres_1():
    nombres = [iloc[:, 0]]
    for i in naves:
        nombres.append(i["Nombre"])
    nombres.sort()
    print(nombres)
    
def ordenar_nombres_2():
    nombres = []
    for i in naves:
        nombres.reverse(i.nombre)
        print(nombres)


a = Nave("Estrella de la muerte", 500, 8998, 69420)
b = Nave("Halcon milenario", 1234, 1059, 1919191)
c = Nave("Lanzador imperial", 9999, 222, 37201)
d = Nave("Destructor estelar", 3721, 3939, 77777)
e = Nave("Supremacy", 56565, 12198, 66666)


def ejecucion3():
        
    ordenar_nombres()


    imprimirNaves()
    ordenar_nombres_1()



