#-*- coding: utf-8 -*-
from fifa21 import *

def mostrar_estadisticas(coleccion):
    i=0
    
    for f in coleccion:
        i = i + 1
        print(i, f)

def test_leer_fifa21(FIFA):
    print('Leidos' , len(FIFA), 'datos de Fifa 21')
    mostrar_estadisticas(FIFA)
    
    print('Primeros tres datos de Fifa 21: ')
    print(FIFA[0])
    print(FIFA[1])
    print(FIFA[2])
    
    print('Últimos tres datos de Fifa 21: ')
    print(FIFA[-3])
    print(FIFA[-2])
    print(FIFA[-1])
###Entrega2
#bloque1
def mostrar_registros (lista):
    for indx, FIFA in enumerate(lista):
        print(f"{indx+1}-{FIFA}")

def test_mostrar_name(FIFA, nacionalidad, edad1 ,edad2 ):
    res = seleccion_jugadores_nacionalidad_edad(FIFA, nacionalidad, edad1, edad2)
    print(f'Hay {len(res)} jugadores de nacionalidad {nacionalidad} con edades entre {edad1} y {edad2} años en Fifa 21')
    mostrar_registros(res)

# Bloque 2 
def test_mostrar_posicion(FIFA, posicion ):
    res = seleccionar_mostrar_posicion(FIFA,posicion) 
    print (f"Hay {res} jugadores con posición {posicion}")
    
#
def test_mostrar_equipos(FIFA):
    res = nombre_de_equipos_de_fifa(FIFA)
    print(f'Los distintos equipos que hay en Fifa 21 son:')
    mostrar_estadisticas(res)
# Bloque 3
def test_calcula_porcentaje_media(FIFA, team):
    res = calcula_porcentaje_de_jugadores_con_buena_media (FIFA, team)
    print(f"El porcentaje de jugadores con una media superior a 70 es del {res:.2f}%")
 
#
def test_calcula_numero_jugadores(FIFA, team):
    res = calcula_numero_de_jugadores_en_un_equipo (FIFA, team)
    print(f"El {team}, tiene {res} jugadores registrados en Fifa 21")
###Entrega 3
#Bloque 4
def test_obten_registro_cantidad_de_jugadores(FIFA):
    nacionalidad = obten_registro_cantidad_de_jugadores(FIFA)
    print(f'El pais con más jugadores registrados es {nacionalidad[0]} con {nacionalidad [1]} jugadores')     
#Bloque 5
def test_menos_media(FIFA, position ='RW',n =4):
    res= menos_media(FIFA)
    print(f'Los {n} jugadores de la posicion {position} con menos media son: ')
    mostrar_registros(res)
#Bloque 6   
def test_jugadores_posicion(FIFA, hits):
    dicc=jugadores_posicion(FIFA, hits)
    print(dicc)
#
def test_top_diccionario_clave_equipo(FIFA, team, n):
    print(f'El diccionario con {team} como clave y sus {n} jugadores con mayor edades son:  ')
    print(top_diccionario_clave_equipo(FIFA, team, n))

if __name__ == '__main__':
    FIFA = lee_fifa('Data/Fifa21/fifa21.csv')
    #test_leer_fifa21(FIFA)
    #test_mostrar_name(FIFA, nacionalidad= 'Argentina', edad1=25, edad2=35)
    #test_mostrar_posicion(FIFA, posicion= 'GK')
    #test_mostrar_posicion(FIFA, posicion= 'ST')
    #test_calcula_porcentaje_media(FIFA, team="Mosqueo")
    #test_calcula_numero_jugadores(FIFA, team="Paris Saint-Germain ")
    #test_calcula_numero_jugadores(FIFA, team= "Real Madrid ")
    #test_mostrar_equipos(FIFA)
    #test_obten_registro_cantidad_de_jugadores(FIFA)
    #test_menos_media(FIFA, position ='RW',n =4) 
    #test_jugadores_posicion(FIFA, hits=68)
    #test_top_diccionario_clave_equipo(FIFA, team ="FC Barcelona " , n = 4)
    
    
    
    