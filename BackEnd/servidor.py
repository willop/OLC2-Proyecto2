#from sklearn import linear_model
#reg = linear_model.LinearRegression()
#reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
#print(reg.coef_)
import base64
from flask import Flask,jsonify,request,json
from flask_cors import CORS


#import para utilizar scikit-learn
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import re
#%matplotlib inline



app = Flask(__name__)
CORS(app)

#variable global variables
archivoglobal = ""
encabezados = ""
ecuacion = ""
valor_r =""
aproximaciones = ""
imagenbase64 = ""

# creando rutas

@app.route('/ping')
def ping():
    return jsonify({"mensaje":"pong!"})

@app.route('/cargamasiva',methods=['POST'])
def cargamasiva():
    global archivoglobal
    archivoglobal = request.files['files']
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
    print("Hola mundo\n\n\n")
    datos=""
    datos = request.get_data()
    print(datos)
    datos=datos.decode('utf-8')
    datos = json.loads(datos)
    print(datos)

    variables = {
        "varcolpais":datos['varcolpais'],
        "varpais":datos['varpais'],
        "variable1": datos['variable1'],
        "variable2": datos['variable2'],
    }
    global archivoglobal
    varcolpais = variables['varcolpais']
    varpais = variables['varpais']
    var1 = variables['variable1']
    var2 = variables['variable2']
    print("hola variable1: "+var1)
    print("hola variable2: "+var2)

    if varpais == "null" or varcolpais == "null":
        print('El archivo viene sin pais')
        df = pd.DataFrame(archivoglobal)
        x = df[var1]
        y = df[var2]
        regr = linear_model.LinearRegression()

        intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        intxx = intxx[:,np.newaxis]  
        print(intxx)
        print(regr.fit(intxx,y))
        print(regr.coef_)
        m=regr.coef_[0]
        b=regr.intercept_
        yaprox= m*intxx+b #prediccion
        ecuacion = 'y={0}*x+{1}'.format(m,b)
        print('y={0}*x+{1}'.format(m,b))
        aproximaciones =regr.predict(intxx)[0:5]
        print(regr.predict(intxx)[0:5])
        valor_r=r2_score(y,yaprox)
        print("El valor de r^2: ",r2_score(y,yaprox))
        plt.scatter(x,y,color='blue')
        plt.plot(x,yaprox,color='red')
        plt.title('Tendecia por Covid-19 en un pais')
        plt.xlabel(var1)
        plt.ylabel(var2)
        #plt.show()
        plt.savefig('./reporte.png')
        #imagenbase64=""
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()

        

    else:
        print('Filtremos el pais')
        newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
        df = pd.DataFrame(newdata)
        x = df[var1]
        y = df[var2]
        regr = linear_model.LinearRegression()      #instacio la regresion

        
        intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        intxx = intxx[:,np.newaxis]                  #CREO MI ARRAY PARA LOS DEMAS CALCULOS 
        print("Imprimiendo la matriz en int")
        print(intxx)
        print(regr.fit(intxx,y))
        print(regr.coef_)
        m=regr.coef_[0]
        b=regr.intercept_
        print("valor de la pendiente")
        print(m)
        print("valor de b")
        print(b)

        yaprox= m*intxx+b #prediccion
        ecuacion = 'y={0}*x+{1}'.format(m,b)
        print('y={0}*x+{1}'.format(m,b))
        aproximaciones =regr.predict(intxx)[0:5]
        print(regr.predict(intxx)[0:5])
        valor_r=r2_score(y,yaprox)
        print("El valor de r^2: ",r2_score(y,yaprox))
        plt.scatter(x,y,color='blue')                 #fecha
        plt.plot(x,yaprox,color='red')
        plt.title('Tendecia por Covid-19 en un pais')
        plt.xlabel(var1)
        plt.ylabel(var2)
        #plt.show()
        plt.savefig('./reporte.png')
        #imagenbase64=""
        with open('./reporte.png',"rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()

    return jsonify({"img": imagenbase64,"ecuacion":ecuacion,"val_r":str(valor_r),"aproximaciones":str(aproximaciones)})


if __name__ == '__main__':
    app.run(debug=True,port=4000)
