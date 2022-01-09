#-*- coding: utf-8 -*-

import csv
from collections import namedtuple
from typing import Counter

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

################################################## Entrega 2 
#bloque 1
def seleccion_jugadores_nacionalidad_edad (fifa21, nacionalidad, edad1, edad2):
    res = [t for t in fifa21 if t.nationality==nacionalidad and t.age >=edad1 and t.age<=edad2]
    return res
#bloque2

def seleccionar_mostrar_posicion(FIFA, posicion):
    res1=0
    for t in FIFA:
        if t.position==posicion:
            res1=res1+1
    return res1
#
def nombre_de_equipos_de_fifa(FIFA):
    return { f.team for f in FIFA }



#BLOQUE 3
def calcula_porcentaje_de_jugadores_con_buena_media(FIFA,team):
    encima_media=0
    total_jugadores=0
    
    for t in FIFA:
        if t.team !=team:
            total_jugadores+=1
            if t.overall >70:
                encima_media+=1
    
    res=None            
    if encima_media >0: 
        res=encima_media*100 /total_jugadores 
    return res
#

def calcula_numero_de_jugadores_en_un_equipo(FIFA,team):
    jugadores_del_equipo=0
    
    for f in FIFA:
        if f.team != team:
            jugadores_del_equipo+=0
        else:
            jugadores_del_equipo+=1
    
    res= jugadores_del_equipo            
    return res

######################## Entrega 3
#Bloque 4
def obten_registro_cantidad_de_jugadores(FIFA):
    nacionalidad = [f.nationality for f in FIFA]
    contador = Counter(nacionalidad)
    dict_contador= dict(contador)
    lista_contador= [tupla for tupla in dict_contador.items()]
    return max(lista_contador, key = lambda x: x[1])
#Bloque 5
def menos_media(FIFA, position ='RW',n =4):
    res =sorted((g for g in FIFA if g.position==position), key=lambda g:g.overall)
    return res[:n]
#Bloque 6
def jugadores_posicion(FIFA, hits):
    dicc={}
    for f in FIFA:
        if f.hits==hits:
            if f.name in dicc:
                dicc[f.name]==f.hits
            else:
                dicc[f.name]= f.hits
    return dicc
#
def top_diccionario_clave_equipo(FIFA, team, n):
    ordenar = sorted([ d for d in FIFA], key= lambda x: x.age, reverse=True)
    diccionario= dict()
    for f in ordenar:
        if team == f.team:
            if f.team not in diccionario:
                diccionario[team] = [f]
            elif f.team == team:
                diccionario[team].append(f)
    return diccionario[team][:n]