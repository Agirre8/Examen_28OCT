from turtle import end_fill
from Ejercicios.Ej1 import Ejercicio1 as ej1
from Ejercicios.Ej2 import Ejercicio2 as ej2

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
        return

    elif n==4:
        return

    elif n==5:
        return

    else:
        print("El numero de ejercicio que has insertado es incorrecto!!!!")

