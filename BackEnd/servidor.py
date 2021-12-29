#from sklearn import linear_model
#reg = linear_model.LinearRegression()
#reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
#print(reg.coef_)

from flask import Flask,jsonify,request,json
from flask_cors import CORS


#import para utilizar scikit-learn
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
#%matplotlib inline



app = Flask(__name__)
CORS(app)

#variable global variables
extensionarchivo = ""
archivoglobal = ""
encabezados = ""

# creando rutas

@app.route('/ping')
def ping():
    return jsonify({"mensaje":"pong!"})

@app.route('/cargamasiva',methods=['POST'])
def cargamasiva():
    global archivoglobal,encabezados
    archivoglobal = request.files['files']
    global extensionarchivo
    extensionarchivo = archivoglobal.filename
    extensionarchivo = extensionarchivo.split('.')[1]
    if extensionarchivo == "json":
        print("es un json")
        archivoglobal = pd.read_json(archivoglobal)
        encabezados = archivoglobal.head(0)
    elif extensionarchivo=="csv":
        print("es un csv")
        archivoglobal = pd.read_csv(archivoglobal)
        encabezados = archivoglobal.keys()
    else:
        archivoglobal = pd.read_excel(archivoglobal)
        encabezados = archivoglobal.head(0)
    print("\npaquete recibido!!!\n")
    return jsonify({"mensaje":"confirmacion!"})

@app.route('/consulta1', methods=['POST'])
def consulta1():
    variables = {
        "varpais":request.json['varpais'],
        "variable1": request.json['variable1'],
        "variable2": request.json['variable2'],
    }
    global encabezados
    varpais = variables['varpais']
    var1 = variables['variable1']
    var2 = variables['variable2']
    print("hola variable1: "+var1)
    print("hola variable2: "+var2)
    print(encabezados)

    if varpais == 'null':
        print('El archivo viene sin pais')
        df = pd.DataFrame(archivoglobal)
        x = df[var1]
        y = df[var2]
        regr = linear_model.LinearRegression()

        xx = x[:,np.newaxis]
        print(xx)
        print(regr.fit(xx,y))
        print(regr.coef_)
        m=regr.coef_[0]
        b=regr.intercept_
        yaprox= m*xx+b #prediccion
        print('y={0}*x+{1}'.format(m,b))
        print(regr.predict(xx)[0:5])
        print("El valor de r^2: ",r2_score(y,yaprox))
        plt.scatter(x,y,color='blue')
        plt.plot(x,yaprox,color='red')
        plt.title('Tendecia por Covid-19 en un pais')
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.show()
        
        
        
        
    else:
        print('Filtremos el pais')
        newdata = archivoglobal.loc[archivoglobal.Ciudad==varpais,:]
        newdata.plot(x=var1 , y=var2, style='o')
        plt.title('Tendecia por Covid-19 en '+varpais)
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.show()

    return jsonify({"mensaje":"pong!"})


if __name__ == '__main__':
    app.run(debug=True,port=4000)
