import numpy as np
def crear_matriz(self):
    
    self.matriz = np.array([[55, 25, 15], 
                    [30, 44, 2], 
                    [11, 45, 77]])

def determinant_fast(A):
    # Section 1: Establish n parameter and copy A
    n = len(A)
    AM = copy_matrix(A)
 
    # Section 2: Row ops on A to get in upper triangle form
    for fd in range(n): # A) fd stands for focus diagonal
        for i in range(fd+1,n): # B) only use rows below fd row
            if AM[fd][fd] == 0: # C) if diagonal is zero ...
                AM[fd][fd] == 1.0e-18 # change to ~zero
            # D) cr stands for "current row"
            crScaler = AM[i][fd] / AM[fd][fd] 
            # E) cr - crScaler * fdRow, one element at a time
            for j in range(n): 
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
     
    # Section 3: Once AM is in upper triangle form ...
    product = 1.0
    for i in range(n):
        # ... product of diagonals is determinant
        product *= AM[i][i] 
 
    return product