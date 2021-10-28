#-*- coding: utf-8 -*-
from fifa21 import *

def mostrar_estadisticas(coleccion):
    i=0
    
    for f in coleccion:
        i = i + 1
        print(i, f)

def test_leer_fifa21():
    print('Leidos' , len(fifa), 'datos de Fifa 21')
    mostrar_estadisticas(fifa)
    
    print('Primeros tres datos de Fifa 21: ')
    print(fifa[0])
    print(fifa[1])
    print(fifa[2])
    
    print('Últimos tres datos de Fifa 21: ')
    print(fifa[-3])
    print(fifa[-2])
    print(fifa[-1])
    
if __name__ == '__main__':
    fifa = lee_fifa('data/Fifa21/fifa21.csv')
    
    test_leer_fifa21()