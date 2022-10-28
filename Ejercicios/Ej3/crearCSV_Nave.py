import csv
from random import *
def crear_csv():
    header = ['Nombre', 'largo', 'tripulcion', 'pasajeros']
    data = [
        ['Halcón Milenario', randint(1,1000), randint(1,1000), randint(1,1000)],
        ['Ala-X / X-Wing', randint(1,1000), randint(1,1000), randint(1,1000)],
        ['Caza TIE / TIE Fighter', randint(1,1000), randint(1,1000), randint(1,1000)],
        ['Destructor Estelar', randint(1,1000), randint(1,1000), randint(1,1000)],
        ['Lanzadera imperial', randint(1,1000), randint(1,1000), randint(1,1000)],
        ['Nave Real Nubian 327 tipo J', randint(1,1000), randint(1,1000), randint(1,1000)],
        ['Nave de Control de Droides clase Lucrehulk', randint(1,1000), randint(1,1000), randint(1,1000)],
        ['Supremacy', randint(1,1000), randint(1,1000), randint(1,1000)],
        ['Speeders', randint(1,1000), randint(1,1000), randint(1,1000)],
        ['Sandcrawler', randint(1,1000), randint(1,1000), randint(1,1000)],
        ['AT-AT', randint(1,1000), randint(1,1000), randint(1,1000)],
    ]

    with open('naves.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
    
crear_csv()