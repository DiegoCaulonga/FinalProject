![image](https://user-images.githubusercontent.com/69120593/96193429-6ca8dd00-0f48-11eb-9cbd-3cdf84d9b0c4.png)
# FinalProject-Desbancando William Hill
Para realizar mi proyecto final, he llevado a cabo tres pasos principales, los cuales podrán encontrar desglosados dentro de la carpeta "src" de la rama "API" de este mismo repositorio. Si no saben como llegar, al estár poco familizarizados con GitHub, la dirección sería la siguiente: https://github.com/DiegoCaulonga/FinalProject-Desbancando_WilliamHill/tree/API/src. He utilizado cada uno de estos pasos, para conseguir obtener el objetivo de mi proyecto, que es realizar, utilizando algorítmos de Machine Learning, una serie de predicciones a cerca de resultados que se darán en La Liga Santander ésta temporada, y con ellos, analizar cuales son las cuotas más interesantes que la casa de apuestas William Hill, ofrece a sus clientes a dia de hoy. Para entender mejor que he hecho en cada uno de mis pasos, voy a explicar para que sirve el codigo que se encuentra en ellos.

## Predictions
En este paso, el objetivo era en primer lugar obtener toda la informacion necesaria para entrenar el algorítmo, y en segundo lugar entrenarlo para obtener las predicciones sobre las cuales posteriormente realizariamos el analisis de las cuotas. 

### Functions.ipynb
Lo primero que hice, fue crear un pipeline con el cual, introduciendo jornada y dato, sustraer toda la información que consideraba discriminante para el algorítmo (datos de la jornada 5) de la API utilizada, y el dato a estudiar en cada caso (datos de la jornada 38). Al necesitar para el proyecto 3 datos (posición en la ultima jornada, puntos en la última jornada, y goles en la ultima jornada), el pipeline te permite obtener cualquiera de ellos, si al segundo argumento de la funcion lo llamabas "pos","points" o "goals" respectivamente.

### Train creation.ipynb
Aquí, apliqué el pipeline a todas las temporadas disponibles, para obtener todos los datos discriminantes de los diferentes equipos en la jornada 5 (posición, puntos, victorias, derrotas, empates, goles a favor, y goles en contra) y los resultados que habían obtenido teniendo esas premisas, de posición, puntos y goles en la jornada 38. Uní, diferenciando por dato de la jornada 38, todas las tablas obtenidas, creando 3 csv: Position.csv, Goals.csv y Points.csv

### X_test creation.ipynb
Para poder entrenar el algorítmo y obtener unas predicciones sobre que pasaría esta temporada con la posición, los puntos, y los goles de los diferentes equipos de La Liga Santander, tenía que sustraer de la API también, los datos discriminantes de los equipos a estudiar a día de hoy, en la jornada 5 de la temporada 2020/2021.

### Algorithm training.ipynb
En este documento, y utilizando todos los datos obtenidos previamente, entreno el algorítmo ExtraTreeClassifier. Esto me sirvió para obtener las predicciones que la inteligencia artificial cree que deberían pasar al final de esta temporada, teniendo en cuenta como se desarrollaron las anteriores, y como va la actual.

## Scraping
En este paso, el objetivo era utilizar técnicas de Web Scraping para obtener todas las cuotas de William Hill que quería analizar. Para mi estudio, he requerido de las cuotas que se referian a los sucesos de: que un equipo quedara entre los cuatro mejores al terminar la competiciones, el descenso de los distintos equipos de La Liga, y para la proxima jornada (Jornada 5), que se marcaran 3 o mas goles en los distintos partidos. 
El proceso para la creación de los csv en los que he recogido las cuotas ha sido muy similar en los 3 casos: hacer un request a la URL, formatear el contenido con BeautifulSoup, y limpiar el contenido para obtener las cuotas y los nombres de los equipos de manera limpia. Para observar el codigo exacto, entrar en: 
"2,5 goles.ipynb", "Descenderán.ipynb" y "Quedarán entre los 4 primeros.ipynb".

## App
En este, el último paso, el objetivo era generar, mediante los datos obtenidos previamente, una base de datos visual en la que poder observar las cuotas recomendadas basándonos en los resultados obtenidos gracias al Machine Learning. Para ello, hemos repartido el proceso en dos etapas:

### Fee and Predictions Fusion.ipynb
En este documento, he fusionado las predicciones obtenidas en el paso "Predictions", con las cuotas obtenidas en el paso "Scraping", para obtener las tablas con las que informaremos a nuestros clientes de cuales son las cuotas mas recomendables segun los distintos sucesos predecidos.

### endpoints.py
En este último archivo, y utilizando Flask, genero una API donde se recogen los análisis generados. La direccion URL de la API es la siguiente: http://diegocaulonga.pythonanywhere.com/
Para observar los análisis ofrecidos, habrá que añadir una serie de endpoints a la URL adjuntada.

1. Los datos utilizados como argumento para el algoritmo de Machine Learning y las predicciones principales obtenidas (endpoint= /datos/) *Adjunto la URL completa que deberian meter a modo de ejemplo: diegocaulonga.pythonanywhere.com/datos 

2.Las totalidad de las predicciones obtenidas (endpoint= /predicciones/) 

3.Los equipos que descenderán y sus respectivas cuotas si el evento se cumpliera (endpoint= /descensos/) 

4.Los equipos que quedarán entre los 4 primeros puestos y sus respectivas cuotas si el evento se cumpliera (endpoint = /primeros4) 

5.Los partidos de la próxima jornada, las cuotas que rodean a la posibilidad de que se marquen 3 o más goles en ellos, y los goles que calculamos que se marcarán en el partido (endpoint = /3goles/). 

*En el caso de los descensos, y los primeros4, las URLs tienen la posibilidad de añadir un endpoint mas (/favoritos/) en el que se podrá encontrar la cuota favorita en cada caso.
