import sys
import unittest
import Ejercicio1 as e1

sys.path.insert(0,"/Users/smite/Documents/GitHub/Prueba-28-oct")

class TestEjercicio1(unittest.TestCase):
    def excepcion_discos(self):
        numero = False
        while numero == False:
            try:
                if e1.n > 74:
                    return print("Numero demasiado grande o demasiado pequeño")
                else:
                    numero == True
            except:
                break
