# FinalProject-Desbancando William Hill
Para realizar mi proyecto final, he llevado a cabo tres pasos principales, los cuales podrán encontrar desglosados dentro de la carpeta "src" de la rama "API" de este mismo repositorio. Si no saben como llegar, al estár poco familizarizados con GitHub, la dirección sería la siguiente: https://github.com/DiegoCaulonga/FinalProject-Desbancando_WilliamHill/tree/API/src. He utilizado cada uno de estos pasos, para conseguir obtener el objetivo de mi proyecto, que es realizar, utilizando algorítmos de Machine Learning, una serie de predicciones a cerca de resultados que se darán en La Liga Santander ésta temporada, y con ellos, analizar cuales son las cuotas más interesantes que la casa de apuestas William Hill, ofrece a sus clientes a dia de hoy. Para entender mejor que he hecho en cada uno de mis pasos, voy a explicar para que sirve el codigo que se encuentra en ellos.

## Functions
En este paso, el objetivo era en primer lugar obtener toda la informacion necesaria para entrenar el algorítmo, y en segundo lugar entrenarlo para obtener las predicciones sobre las cuales posteriormente realizariamos el analisis de las cuotas. 

### Functions.ipynb
Lo primero que hice, fue crear un pipeline con el cual, introduciendo jornada y dato, sustraer toda la información que consideraba discriminante para el algorítmo (datos de la jornada 5) de la API utilizada, y el dato a estudiar en cada caso (datos de la jornada 38). Al necesitar para el proyecto 3 datos (posición en la ultima jornada, puntos en la última jornada, y goles en la ultima jornada), el pipeline te permite obtener cualquiera de ellos, si al segundo argumento de la funcion lo llamabas "pos","points" o "goals" respectivamente.

### Train creation.ipynb
Aquí, apliqué el pipeline a todas las temporadas disponibles, para obtener todos los datos discriminantes de los diferentes equipos en la jornada 5 (posición, puntos, victorias, derrotas, empates, goles a favor, y goles en contra) y los resultados que habían obtenido teniendo esas premisas, de posición, puntos y goles en la jornada 38. Uní, diferenciando por dato de la jornada 38, todas las tablas obtenidas, creando 3 csv: Position.csv, Goals.csv y Points.csv

### X_test creation
Para poder entrenar el algorítmo y obtener unas predicciones sobre que pasaría esta temporada con la posición, los puntos, y los goles de los diferentes equipos de La Liga Santander, tenía que sustraer de la API también, los datos discriminantes de los equipos a estudiar a día de hoy, en la jornada 5 de la temporada 2020/2021.

### Algorithm training
En este documento, y utilizando todos los datos obtenidos previamente, entreno el algorítmo ExtraTreeClassifier. Esto me sirvió para obtener las predicciones que la inteligencia artificial cree que deberían pasar al final de esta temporada, teniendo en cuenta como se desarrollaron las anteriores, y como va la actual.

## Scraping
