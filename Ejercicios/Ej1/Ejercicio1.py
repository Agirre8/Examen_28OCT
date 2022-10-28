def FuncionOrdenar(n , inicio, destino, auxiliar):
    if n==1:
        print (f"Mover disco desde inicio {inicio} a su destino{destino}")
        return
    FuncionOrdenar(n-1, inicio, auxiliar, destino)
    print (f"Mover disco {n} desde inicio {inicio} al destino {destino}")
    FuncionOrdenar(n-1, auxiliar, destino, inicio)

n=4
FuncionOrdenar(n,'A','B','C')

   





    




  
