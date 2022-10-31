import sys
# from Ejercicios.Ej1 import Ejercicio1 as ej1
# from Ejercicios.Ej2 import Ejercicio2 as ej2
# from Ejercicios.Ej3 import Ejercicio3 as ej3
# from Ejercicios.Ej4 import Ejercicio4 as ej4
# from Ejercicios.Ej5 import Ejercicio5 as ej5


sys.path.insert(0,"/Users/smite/Documents/GitHub/Examen_28OCT/Ejercicios/Ej3")
sys.path.insert(0,"/Users/smite/Documents/GitHub/Examen_28OCT/Ejercicios/Ej1")
sys.path.insert(0,"/Users/smite/Documents/GitHub/Examen_28OCT/Ejercicios/Ej2")
sys.path.insert(0,"/Users/smite/Documents/GitHub/Examen_28OCT/Ejercicios/Ej4")
sys.path.insert(0,"/Users/smite/Documents/GitHub/Examen_28OCT/Ejercicios/Ej5")
from Ejercicio1 import *
from Ejercicio2 import *
from Ejercicio3 import *
from Ejercicio4 import *
from Ejercicio5 import *

def ejecutar():
    n = input("Inserte el numero de el ejercicio que quieras ejecutar:")

    if n == 1:
        n = 4
        FuncionOrdenar(n,'A','B','C')

    elif n==2:
            
        mat = [[1, 0, 2, -1],
            [3, 0, 0, 5],
            [2, 1, 4, -3],
            [1, 0, 5, 0]]

        print('El determinante de la matriz es:', determinantOfMatrix(mat))


    elif n==3:
        ejecucion3()
 

    elif n==4:
        ejecucion4()

    elif n==5:
        ejecucion5()

    else:
        print("El numero de ejercicio que has insertado es incorrecto!!!!")

