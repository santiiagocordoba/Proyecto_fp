#-*- coding: utf-8 -*-

import csv
from collections import namedtuple

Fifa21 = namedtuple ('Fifa21','player_id, name, nationality, position, overall, age, hits, potential, team')

## EJERCICIO 1
def lee_fifa(fichero):
    lista_tupla=[]
    with open(fichero, encoding='utf-8') as f:
        lector=csv.reader(f,delimiter= ';')
        next(lector)
        for linea in lector:
            player_id = int(linea[0])
            name = linea[1]
            nationality = linea[2]
            position = linea[3]
            overall = int(linea[4])
            age = int(linea[5])
            hits = int(linea[6])
            potential = int(linea[7])
            team = linea[8]
            
            tupla = Fifa21(player_id,name,nationality,position,overall,age,hits,potential,team)
            lista_tupla.append(tupla)
    return lista_tupla