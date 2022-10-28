from nave import *
        
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
ordenar_nombres()



