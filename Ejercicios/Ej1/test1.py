import sys
import unittest
import Ejercicio1 as e1

sys.path.insert(0,"/Users/smite/Documents/GitHub/Examen-28OCT")

class TestEjercicio1(unittest.TestCase):
    def excepcion_discos(self):
        numero = False
        while numero == False:
            try:
                if e1.n > 20:
                    return print("Numero demasiado grande o demasiado pequeño")
                else:
                    numero == True
            except:
                break
