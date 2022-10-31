
import sympy

P1 = input("Primer Polinomio: ")
P2 = input("Segundo Polinomio: ")
print("n")


sympy.init_printing()
x,y = sympy.symbols('x,y')

#almacenamos en variables los dos polinomios procesados por la función Poly de sympy 
Poly1 = sympy.Poly(P1)
Poly2 = sympy.Poly(P2)

#funciones para hacer las operaciones que deseeemos
def mult(p1, p2):
    return p1 * p2
def suma(p1, p2):
    return p1 + p2
def res(p1, p2):
    return p1 - p2
def div(p1, p2):
    return p1 / p2

def ejecucion4():
    
    print("Resultado: ", mult(Poly1, Poly2))

