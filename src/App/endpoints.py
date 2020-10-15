import pandas as pd
import os
from flask import Flask, request
from flask import render_template
app = Flask(__name__)

PATH = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    return """Bienvenidos a mi API de análisis de las cuotas de William Hill para La Liga Santander. 
    En ella, podrán hacer un recorrido por una serie de tablas, en las  que se representarán cuales 
    son las predicciones que mediante algorítmos de  Machine Learning, hemos obtenido sobre distintos 
    resultados de La Liga, y cuales  son las cuotas establecidas por la casa de apuestas William Hill 
    para el caso de que  se cumplieran esos resultados. Para observar estas tablas, habrá que modificar 
    los  endpoints del URL de esta API. Los análisis disponibles son los siguientes: 1.Los datos utilizados 
    como argumento para el algoritmo de Machine Learning y las  predicciones principales obtenidas (endpoint= /datos/) 
    2.Las totalidad de las predicciones obtenidas (endpoint= /predicciones/) 3.Los equipos que descenderán y sus respectivas 
    cuotas si el evento se cumpliera (endpoint= /descensos/) 4.Los equipos que quedarán entre los 4 primeros puestos y 
    sus respectivas cuotas  si el evento se cumpliera (endpoint = /primeros4) 5.Los partidos de la próxima jornada, las 
    cuotas que rodean a la posibilidad de que se marquen 3 o más goles en ellos, y los goles que calculamos que se marcarán 
    en el  partido (endpoint = /3goles/). En el caso de los descensos, y los primeros4, las URLs  tienen la posibilidad de 
    añadir un endpoint mas (/favoritos/) en el que se podra encontrar la cuota mejor pagada."""
    
@app.route('/datos/')
def dato():
    datosof = pd.read_csv(PATH+"../Predictions/ClasOficial.csv").drop(columns=["Unnamed: 0"])
    return datosof.to_html()

@app.route('/predicciones/')
def pred():
    predicciones = pd.read_csv(PATH+"../Predictions/Predictions.csv").set_index("Position")
    return predicciones.to_html()

@app.route('/descensos/')
def desc():
    descensos = pd.read_csv(PATH+"Descensos.csv").drop(columns=["Position"])
    return descensos.to_html()

@app.route('/descensos/favorita/')
def descf():
    descensosf = pd.read_csv(PATH+"Descensos.csv").drop(columns=["Position"])
    descensosF = descensosf.sort_values(by="Cuotas",ascending=False).head(1)

@app.route('/primeros4/')
def prim4():
    primeros = pd.read_csv(PATH+"Primeros4.csv").drop(columns=["Position"])
    return primeros.to_html()

@app.route('/primeros4/favorita/')
def prim4f():
    primerosf = pd.read_csv(PATH+"Primeros4.csv").drop(columns=["Position"])
    primerosF = primerosf.sort_values(by="Cuotas",ascending=False).head(1)
    return primerosF.to_html()

@app.route('/3goles/')
def goles3():
    golestres = pd.read_csv(PATH+"TresGoles.csv").drop(columns=["Unnamed: 0"])
    golestres = golestres.rename(columns={"cuota-2,5":"cuota <3 goles","cuota+2,5":"cuota >=3 goles","Goles Partido":"Predicción nºGoles"})
    return golestres.to_html()
    
if __name__=="__main__":
    app.run(debug=False)