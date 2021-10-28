[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5942112&assignment_repo_type=AssignmentRepo)
## Carpeta src

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<fifa21.py\>**: Este módulo contiene los datos de los jugadores de Fifa21.
  * **\<fifa21test.py\>**: Este módulo contiene el código test de los datos de los jugadores de Fifa21.
  * **\<modulo2.py\>**: Añade descripciones para el resto de módulos que pueda tener tu proyecto. Por ejemplo, sería conveniente tener un módulo separado con funciones genéricas para dibujar gráficas y/o otro con funciones genéricas de conversión de tipos. 
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<fifa21.csv\>**: En este archivo o fichero '.csv' está presente los datos de los jugadores.
    
## Estructura del *dataset*

Aquí debes describir la estructura del dataset explicando qué representan los datos que contiene y la descripción de cada una de las columnas.

El dataset está compuesto por \<9\> columnas, con la siguiente descripción:

* **\<player_id>**: de tipo \<int\>, El código que reprensenta el fútbolista en el Fifa.
* **\<name>**: de tipo \<str\>, Nombre del fútbolista.
* **\<nationality>**: de tipo \<str\>, País del fútbolista en el nació o representa en la selección.
* **\<position>**: de tipo \<str\>, Posición en la que juega o puede jugar el fútbolista en el juego.
* **\<overall>**: de tipo \<int\>, Media del conjunto de las estadisticas que tiene el jugador.
* **\<age>**: de tipo \<int\>, Edad que tiene los fútbolistas dentro del juego.
* **\<hits>**: de tipo \<int\>, Influencia o reconocimiento a nivel global del jugador
* **\<potential>**: de tipo \<int\>, Es la media que podrá llegar a conseguir el fútbolista en el juego.
* **\<team>**: de tipo \<str\>, Equipo donde juega el fútbolista.

## Tipos implementados

Fifa21 = namedtuple ('Fifa21','player_id, name, nationality, position, overall, age, hits, potential, team')

#en la que los tipos de cada uno de los campos son los siguientes:
  Fifa21(int,str,str,str,int,int,int,int,str)

Las decisiones de diseño más destacadas de este tipo son:
  -El campo de player_id que es de tipo int ya que es un Integer y en el que en el dataset original aparece como si fuera una 'id'. 

## Funciones implementadas
En este proyecto se han implementado las siguientes funciones. El módulo principal es el módulo fifa21.py, así que aquí es donde se hará referencia a cada uno de los bloques de las entregas.

### \<fifa21.py\>
  #Entrega 1
* **<leer_fifa(fichero)>**: lee los datos del fichero csv 'fifa21.csv'

### \<fifa21test.py\>
  #Entrega1
* **<mostrar_estadisticas(coleccion)>**: Muestra todas las estadisticas que aparecen en el archivo '.csv'
* **<test_leer_fifa21()>**: Lee nuevamente los datos del fichero '.csv' y muestra un print con el número total de estadísticas que dispine el fichero, así mismo muestra las tres primeras y últimas filas de la lista saltandose la primera fila ya que ahí se encuentra los títulos de cada columna
### \<modulo 2\>

* **<funcion 1>**: Descripción de la función 1.
* **<funcion 2>**: Descripción de la función 2.
* ...
