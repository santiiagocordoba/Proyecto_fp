[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5942112&assignment_repo_type=AssignmentRepo)
## Carpeta src

* /src: Contiene los diferentes módulos de Python que conforman el proyecto.
  * fifa21.py: Este módulo contiene los datos de los jugadores de Fifa21.
  * fifa21test.py: Este módulo contiene el código test de los datos de los jugadores de Fifa21.
* /data: Contiene el dataset o datasets del proyecto
    * fifa21.csv: En este archivo o fichero '.csv' está presente los datos de los jugadores.
    

## Estructura del *dataset*

El dataset está compuesto por 9 columnas, con la siguiente descripción:

* player_id: de tipo int, El código que reprensenta el fútbolista en el Fifa.
* name: de tipo str, Nombre del fútbolista.
* nationality: de tipo str, País del fútbolista en el nació o representa en la selección.
* position: de tipo str, Posición en la que juega o puede jugar el fútbolista en el juego.
* overall: de tipo int, Media del conjunto de las estadisticas que tiene el jugador.
* age: de tipo int, Edad que tiene los fútbolistas dentro del juego.
* hits: de tipo int, Influencia o reconocimiento a nivel global del jugador
* potential: de tipo int, Es la media que podrá llegar a conseguir el fútbolista en el juego.
* team: de tipo str, Equipo donde juega el fútbolista.

## Tipos implementados

Fifa21 = namedtuple ('Fifa21','player_id, name, nationality, position, overall, age, hits, potential, team')

#en la que los tipos de cada uno de los campos son los siguientes:
  Fifa21(int,str,str,str,int,int,int,int,str)

Las decisiones de diseño más destacadas de este tipo son:
  -El campo de player_id que es de tipo int ya que es un Integer y en el que en el dataset original aparece como si fuera una 'id'. 

## Funciones implementadas
En este proyecto se han implementado las siguientes funciones. El módulo principal es el módulo fifa21.py, así que aquí es donde se hará referencia a cada uno de los bloques de las entregas.

## Entrega 1
### fifa21.py
* **lee_fifa(fichero)**: lee los datos del fichero csv 'fifa21.csv'

### fifa21test.py
* **mostrar_estadisticas(coleccion)**: Muestra todas las estadisticas que aparecen en el archivo '.csv'
* **test_leer_fifa21()**: Lee nuevamente los datos del fichero '.csv' y muestra un print con el número total de estadísticas que dispine el fichero, así mismo muestra las tres primeras y últimas filas de la lista saltandose la primera fila ya que ahí se encuentra los títulos de cada columna

## Entrega 2
### fifa21.py
* **seleccion_jugadores_nacionalidad_edad (fifa21, nacionalidad, edad1, edad2)**: Lee el fichero 'csv' y selecciona los jugadores que hay en Fifa 21 con la misma nacionalidad y que estan dentro de un rango de edad marcado
* **seleccionar_mostrar_posicion(FIFA, posicion)**: Lee el fichero 'csv' y cuenta el número de jugadores que juegan en una misma posición
* **nombre_de_equipos_de_fifa(FIFA)**: Lee el fichero 'csv' y selecciona el nombre de todos los equipos que aparecen en Fifa 21 sin seleccionar ningún nombre repetido
* **calcula_porcentaje_de_jugadores_con_buena_media(FIFA,team)**: Lee el fichero 'csv' y nos muestra la media de jugadores con una media superior a la seleccionada(en este caso superior a 70)
* **calcula_numero_de_jugadores_en_un_equipo(FIFA,team)**: Lee el fichero 'csv' y nos indica el número de jugadores registrados en Fifa 21 del equipo que hayamos elegido 

### fifa21test.py
* **test_mostrar_name(FIFA, nacionalidad, edad1 ,edad2 )**: Una vez leido el 'csv' muestra todos los nombres de los jugadores en columna juntos a todos sus atributos
* **test_mostrar_posicion(FIFA, posicion )**: Muestra el número de jugadores que juegan en la posición seleccionada 
* **test_mostrar_equipos(FIFA)**: Una vez leido el 'csv' muestra todos los nombres de los equipos en columna
* **test_calcula_porcentaje_media(FIFA, team)**: Una vez seleccionado a todos los jugadores que cumplen con la condición pedida se muestra la la media de jugadores con en forma de porcentaje(%)
* **test_calcula_numero_jugadores(FIFA, team)**: Nos muestra una frase donde nos dice el número de jugadores que dispone el equipo elegido

## Entrega 3
### fifa21.py
* **obten_registro_cantidad_de_jugadores(FIFA)**: Lee el csv y devuelve el país con más jugadores registrados
* **menos_media(FIFA, position ='RW',n =4)**: Lee el csv y devuelve los 'n' jugadores de la posicion que queramos con menos media
* **jugadores_posicion(FIFA, hits)**: Lee el csv y devuelve los jugadores que coinciden con el valor de la clave
* **top_diccionario_clave_equipo(FIFA, team, n)**: Lee el csv y devuelve los 'n' diccionarios filtrados por el valor clave de la función

### fifa21test.py  
* **test_obten_registro_cantidad_de_jugadores(FIFA)**:Muestra el pais con más jugadores registrados registrados en Fifa 21
* **test_menos_media(FIFA, position ='RW',n =4)**: Muestra los 'n' jugadores de la posicion que queramos con menos media
* **test_jugadores_posicion(FIFA, hits)**: Muestra por pantalla los jugadores que coinciden con el valor de la clave
* **test_top_diccionario_clave_equipo(FIFA, team, n)**: Muestra por pantalla los 'n' diccionarios filtrados por el valor clave de la función
