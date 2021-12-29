#from sklearn import linear_model
#reg = linear_model.LinearRegression()
#reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
#print(reg.coef_)

from flask import Flask,jsonify,request,json
from flask_cors import CORS

#import para utilizar scikit-learn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline



app = Flask(__name__)
CORS(app)

#variable global variables
extensionarchivo = ""
archivoglobal = ""


# creando rutas

@app.route('/ping')
def ping():
    return jsonify({"mensaje":"pong!"})

@app.route('/cargamasiva',methods=['POST'])
def cargamasiva():
    global archivoglobal
    archivoglobal = request.files['files']
    global extensionarchivo
    extensionarchivo = archivoglobal.filename
    extensionarchivo = extensionarchivo.split('.')[1]
    if extensionarchivo == "json":
        print("es un json")
        archivoglobal = pd.read_json(archivoglobal)
    elif extensionarchivo=="csv":
        print("es un csv")
        archivoglobal = pd.read_csv(archivoglobal)
    else:
        archivoglobal = pd.read_excel(archivoglobal)
    print("\npaquete recibido!!!\n")
    return jsonify({"mensaje":"confirmacion!"})

@app.route('/consulta1', methods=['POST'])
def consulta1():
    variables = {
        "variable1": request.json['variable1'],
        "variable2": request.json['variable2'],
    }
    print("hola variable1: "+variables['variable1'])
    print("hola variable2: "+variables['variable2'])
    #global archivoglobal
    #print(archivoglobal.shape)
    return jsonify({"mensaje":"pong!"})


if __name__ == '__main__':
    app.run(debug=True,port=4000)
