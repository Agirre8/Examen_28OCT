from turtle import end_fill
from Ejercicios.Ej1 import Ejercicio1 as ej1
from Ejercicios.Ej2 import Ejercicio2 as ej2
from Ejercicios.Ej3 import Ejercicio3 as ej3

def ejecutar():
    n = input("Inserte el numero de el ejercicio que quieras ejecutar:")

    if n == 1:
        n = 4
        ej1.FuncionOrdenar(n,'A','B','C')

    elif n==2:
            
        mat = [[1, 0, 2, -1],
            [3, 0, 0, 5],
            [2, 1, 4, -3],
            [1, 0, 5, 0]]

        print('El determinante de la matriz es:', ej2.determinantOfMatrix(mat))


    elif n==3:
        a = ej3.Nave("Estrella de la muerte", 500, 8998, 69420)
        b = ej3.Nave("Halcon milenario", 1234, 1059, 1919191)
        c = ej3.Nave("Lanzador imperial", 9999, 222, 37201)
        d = ej3.Nave("Destructor estelar", 3721, 3939, 77777)
        e = ej3.Nave("Supremacy", 56565, 12198, 66666)
        ej3.ordenar_nombres()
 

    elif n==4:
        return

    elif n==5:
        return

    else:
        print("El numero de ejercicio que has insertado es incorrecto!!!!")

