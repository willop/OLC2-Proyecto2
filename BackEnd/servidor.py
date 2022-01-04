#from sklearn import linear_model
#reg = linear_model.LinearRegression()
#reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
#print(reg.coef_)
import base64
from flask import Flask,jsonify,request,json
from flask_cors import CORS
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error


#import para utilizar scikit-learn
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import re
from sklearn import preprocessing
import seaborn as sns
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
        archivoglobal = pd.replace({"":0," ":0})
    elif extensionarchivo=="csv":
        print("es un csv")
        archivoglobal = pd.read_csv(archivoglobal)
    else:
        archivoglobal = pd.read_excel(archivoglobal)
    print("\npaquete recibido!!!\n")
    return jsonify({"mensaje":"confirmacion!"})

@app.route('/consulta1', methods=['POST'])
def consulta1():
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
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)

        intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        intxx = intxx[:,np.newaxis]  
        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y,test_size=0.2)

        poli_reg = PolynomialFeatures(degree = 2)
        x_train_poli = poli_reg.fit_transform(x_train_p)
        x_test_poli = poli_reg.fit_transform(x_test_p)

        pr = linear_model.LinearRegression()

        pr.fit(x_train_poli,y_train_p)

        y_pred_pr =pr.predict(x_test_poli)
        print("error")
        print(pr.score(x_train_poli,y_train_p))
        plt.scatter(x,y,color='blue')
        plt.plot(x,y, color='red',linewidth=2)
        plt.title('Tendecia por Covid-19 en un pais')
        plt.xlabel(var1)
        plt.ylabel(var2)
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
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)

        intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        intxx = intxx[:,np.newaxis]  
        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y,test_size=0.6)

        poli_reg = PolynomialFeatures(degree = 2)
        x_train_poli = poli_reg.fit_transform(x_train_p)
        x_test_poli = poli_reg.fit_transform(x_test_p)

        pr = linear_model.LinearRegression()

        pr.fit(x_train_poli,y_train_p)

        y_pred_pr =pr.predict(x_test_poli)
        plt.scatter(x,y,color='blue')
        plt.plot(x,y, color='red',linewidth=2)
        plt.title('Tendecia por Covid-19 en '+str(varpais))
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.savefig('./reporte.png')
        #imagenbase64=""
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()
        
    m=pr.score(x_train_poli,y_train_p)  
    ecuacion = str(round(pr.coef_[1],2))+'x+'+str(round(pr.coef_[2]))+'x^2+'+str(round(pr.intercept_,2))
    valor_r= str(r2_score(y_pred_pr,y_test_p))
    print("El valor de la pendiente es: "+str(m))
    print("El valor de la ecuacion es: "+str(ecuacion))
    return jsonify({"img": imagenbase64,"ecuacion":ecuacion,"val_r":str(valor_r),"pendiente":str(m)})

@app.route('/consulta2', methods=['POST'])
def consulta2():
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
        "cantidad": datos['cantidad']
    }
    global archivoglobal
    varcolpais = variables['varcolpais']
    varpais = variables['varpais']
    var1 = variables['variable1']
    var2 = variables['variable2']
    varcant = variables['cantidad']
    mse=''
    r_cuadrado = ''


    if varpais == "null" or varcolpais == "null":
        print('El archivo viene sin pais')
        df = pd.DataFrame(archivoglobal)
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)

        intxx=np.arange(0,x.size,1)
        #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        print(intxx)
        primerdato = intxx[0]
        ultimo= intxx[intxx.size-1]
        cantidadmas = ultimo + int(varcant)
        print('Ultimo dato ='+ str(ultimo))
        intxx = intxx[:,np.newaxis]  

        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
        x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

        poli = PolynomialFeatures(degree = 2)
        x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)

    	
        pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
        coef = pr.coef_
        print("coeficiente")
        print(coef)
        intercept = pr.intercept_
        auxy = pr.predict(x_train_polinomio)
        mse = np.sqrt(mean_squared_error(y_train_p,auxy))
        r_cuadrado = r2_score(y_train_p,auxy)
        print('r cuadrado')
        print(r_cuadrado)

        nuevo_x = np.arange(primerdato,cantidadmas,1)  #ACA CREO MI NUEVO X                          #lo convierto
        print(nuevo_x)
        print("tamanio"+str(nuevo_x.size))

        response = intercept + coef[1] * nuevo_x+coef[2] * nuevo_x**2  
        valoraprox = response[response.size-1]
        plt.scatter(intxx,y,color='blue')
        plt.plot(nuevo_x,response, color='green',linewidth=3)
        plt.title('Tendecia por Covid-19 en un pais\nLa prediccion del dia '+str(cantidadmas)+' = '+str(valoraprox))
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()

             
       

    else:
        print('Filtremos el pais')
        newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
        df = pd.DataFrame(newdata)
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)
        
        intxx=np.arange(0,x.size,1)
        #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        print(intxx)
        primerdato = intxx[0]
        ultimo= intxx[intxx.size-1]
        cantidadmas = ultimo + int(varcant)
        print('Ultimo dato ='+ str(ultimo))
        intxx = intxx[:,np.newaxis]  

        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
        x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

        poli = PolynomialFeatures(degree = 2)
        x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)


        pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
        coef = pr.coef_
        print("coeficiente")
        print(coef)
        intercept = pr.intercept_
        auxy = pr.predict(x_train_polinomio)
        mse = np.sqrt(mean_squared_error(y_train_p,auxy))
        r_cuadrado = r2_score(y_train_p,auxy)
        print('r cuadrado')
        print(r_cuadrado)

        nuevo_x = np.arange(primerdato,cantidadmas,1)  #ACA CREO MI NUEVO X                          #lo convierto
        print(nuevo_x)
        print("tamanio"+str(nuevo_x.size))

        response = intercept + coef[1] * nuevo_x+coef[2] * nuevo_x**2  
        valoraprox = response[response.size-1]
        plt.scatter(intxx,y,color='blue')
        plt.plot(nuevo_x,response, color='green',linewidth=3)
        plt.title('Tendecia por Covid-19 en '+varpais+'\nLa prediccion del dia '+str(cantidadmas)+' = '+str(valoraprox))       
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()

    ecuacion = str(round(intercept,2))+'+'+ str(round(coef[1],2)) + '* x +'+ str(round(coef[2])) +'x^2'  
    print("El valor de la ecuacion es: "+str(ecuacion))
    return jsonify({"img": imagenbase64,"mse":str(ecuacion),"val_r_cuadrado":str(r_cuadrado)})

@app.route('/consulta3', methods=['POST'])
def consulta3():
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
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)
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
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)
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


    
    return jsonify({"img": imagenbase64,"ecuacion":ecuacion,"indice":str(m)})

@app.route('/consulta4', methods=['POST'])
def consulta4():
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
        "cantidad": datos['cantidad']
    }
    global archivoglobal
    varcolpais = variables['varcolpais']
    varpais = variables['varpais']
    var1 = variables['variable1']
    var2 = variables['variable2']
    varcant = variables['cantidad']
    mse=''
    r_cuadrado = ''

    if varpais == "null" or varcolpais == "null":
        print('El archivo viene sin pais')
        df = pd.DataFrame(archivoglobal)
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)

        intxx=np.arange(0,x.size,1)
        #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        print(intxx)
        primerdato = intxx[0]
        ultimo= intxx[intxx.size-1]
        cantidadmas = ultimo + int(varcant)
        print('Ultimo dato ='+ str(ultimo))
        intxx = intxx[:,np.newaxis]  

        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
        x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

        poli = PolynomialFeatures(degree = 2)
        x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)

    	
        pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
        coef = pr.coef_
        print("coeficiente")
        print(coef)
        intercept = pr.intercept_
        auxy = pr.predict(x_train_polinomio)
        mse = np.sqrt(mean_squared_error(y_train_p,auxy))
        r_cuadrado = r2_score(y_train_p,auxy)
        print('r cuadrado')
        print(r_cuadrado)

        nuevo_x = np.arange(primerdato,cantidadmas,1)  #ACA CREO MI NUEVO X                          #lo convierto
        print(nuevo_x)
        print("tamanio"+str(nuevo_x.size))

        response = intercept + coef[1] * nuevo_x+coef[2] * nuevo_x**2  
        valoraprox = response[response.size-1]
        plt.scatter(intxx,y,color='blue')
        plt.plot(nuevo_x,response, color='green',linewidth=3)
        plt.title('Predicción de mortalidad por COVID en un Departamento\nLa prediccion para el dia '+str(cantidadmas)+' = '+str(valoraprox))
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()

             
       

    else:
        print('Filtremos el pais')
        newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
        df = pd.DataFrame(newdata)
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)
        
        intxx=np.arange(0,x.size,1)
        #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        print(intxx)
        primerdato = intxx[0]
        ultimo= intxx[intxx.size-1]
        cantidadmas = ultimo + int(varcant)
        print('Ultimo dato ='+ str(ultimo))
        intxx = intxx[:,np.newaxis]  

        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
        x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

        poli = PolynomialFeatures(degree = 2)
        x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)


        pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
        coef = pr.coef_
        print("coeficiente")
        print(coef)
        intercept = pr.intercept_
        auxy = pr.predict(x_train_polinomio)
        mse = np.sqrt(mean_squared_error(y_train_p,auxy))
        r_cuadrado = r2_score(y_train_p,auxy)
        print('r cuadrado')
        print(r_cuadrado)

        nuevo_x = np.arange(primerdato,cantidadmas,1)  #ACA CREO MI NUEVO X                          #lo convierto
        print(nuevo_x)
        print("tamanio"+str(nuevo_x.size))

        response = intercept + coef[1] * nuevo_x+coef[2] * nuevo_x**2  
        valoraprox = response[response.size-1]
        plt.scatter(intxx,y,color='blue')
        plt.plot(nuevo_x,response, color='green',linewidth=3)
        plt.title('Predicción de mortalidad por COVID en el Departamento '+varpais+'\nLa prediccion para el dia '+str(cantidadmas)+' = '+str(valoraprox))
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()
    
    
    ecuacion = str(round(intercept,2))+'+'+ str(round(coef[1],2)) + '* x +'+ str(round(coef[2])) +'x^2'  
    print("El valor de la ecuacion es: "+str(ecuacion))
    return jsonify({"img": imagenbase64,"mse":str(ecuacion),"val_r_cuadrado":str(r_cuadrado)})

@app.route('/consulta5', methods=['POST'])
def consulta5():
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
        "cantidad": datos['cantidad']
    }
    global archivoglobal
    varcolpais = variables['varcolpais']
    varpais = variables['varpais']
    var1 = variables['variable1']
    var2 = variables['variable2']
    varcant = variables['cantidad']
    mse=''
    r_cuadrado = ''

    if varpais == "null" or varcolpais == "null":
        print('El archivo viene sin pais')
        df = pd.DataFrame(archivoglobal)
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)

        intxx=np.arange(0,x.size,1)
        #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        print(intxx)
        primerdato = intxx[0]
        ultimo= intxx[intxx.size-1]
        cantidadmas = ultimo + int(varcant)
        print('Ultimo dato ='+ str(ultimo))
        intxx = intxx[:,np.newaxis]  

        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
        x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

        poli = PolynomialFeatures(degree = 2)
        x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)

    	
        pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
        coef = pr.coef_
        print("coeficiente")
        print(coef)
        intercept = pr.intercept_
        auxy = pr.predict(x_train_polinomio)
        mse = np.sqrt(mean_squared_error(y_train_p,auxy))
        r_cuadrado = r2_score(y_train_p,auxy)
        print('r cuadrado')
        print(r_cuadrado)

        nuevo_x = np.arange(primerdato,cantidadmas,1)  #ACA CREO MI NUEVO X                          #lo convierto
        print(nuevo_x)
        print("tamanio"+str(nuevo_x.size))

        response = intercept + coef[1] * nuevo_x+coef[2] * nuevo_x**2  
        valoraprox = response[response.size-1]
        plt.scatter(intxx,y,color='blue')
        plt.plot(nuevo_x,response, color='green',linewidth=3)
        plt.title('Predicción de mortalidad por COVID en un País.\nLa prediccion para el dia '+str(cantidadmas)+' = '+str(valoraprox))
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()

             
       
    else:
        print('Filtremos el pais')
        newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
        df = pd.DataFrame(newdata)
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)
        
        intxx=np.arange(0,x.size,1)
        #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        print(intxx)
        primerdato = intxx[0]
        ultimo= intxx[intxx.size-1]
        cantidadmas = ultimo + int(varcant)
        print('Ultimo dato ='+ str(ultimo))
        intxx = intxx[:,np.newaxis]  

        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
        x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

        poli = PolynomialFeatures(degree = 2)
        x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)


        pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
        coef = pr.coef_
        print("coeficiente")
        print(coef)
        intercept = pr.intercept_
        auxy = pr.predict(x_train_polinomio)
        mse = np.sqrt(mean_squared_error(y_train_p,auxy))
        r_cuadrado = r2_score(y_train_p,auxy)
        print('r cuadrado')
        print(r_cuadrado)

        nuevo_x = np.arange(primerdato,cantidadmas,1)  #ACA CREO MI NUEVO X                          #lo convierto
        print(nuevo_x)
        print("tamanio"+str(nuevo_x.size))

        response = intercept + coef[1] * nuevo_x+coef[2] * nuevo_x**2  
        valoraprox = response[response.size-1]
        plt.scatter(intxx,y,color='blue')
        plt.plot(nuevo_x,response, color='green',linewidth=3)
        plt.title('Predicción de mortalidad por COVID en el pais '+varpais+'\nLa prediccion para el dia '+str(cantidadmas)+' = '+str(valoraprox))
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()

    ecuacion = str(round(intercept,2))+'+'+ str(round(coef[1],2)) + '* x +'+ str(round(coef[2])) +'x^2'  
    print("El valor de la ecuacion es: "+str(ecuacion))
    return jsonify({"img": imagenbase64,"mse":str(ecuacion),"val_r_cuadrado":str(r_cuadrado)})

@app.route('/consulta6', methods=['POST'])
def consulta6():
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
    mse=''
    r_cuadrado = ''


    if varpais == "null" or varcolpais == "null":
        print('El archivo viene sin pais')
        df = pd.DataFrame(archivoglobal)
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)

        intxx=np.arange(0,x.size,1)
        #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        print(intxx)
        intxx = intxx[:,np.newaxis]  

        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
        x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

        poli = PolynomialFeatures(degree = 2)
        x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)

    	
        pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
        coef = pr.coef_
        print("coeficiente")
        print(coef)
        intercept = pr.intercept_
        auxy = pr.predict(x_train_polinomio)
        mse = np.sqrt(mean_squared_error(y_train_p,auxy))
        r_cuadrado = r2_score(y_train_p,auxy)
        print('r cuadrado')
        print(r_cuadrado)


        response = intercept + coef[1] * intxx+coef[2] * intxx**2  
        valoraprox = response[response.size-1]
        plt.scatter(intxx,y,color='blue')
        plt.plot(intxx,response, color='green',linewidth=3)
        plt.title('Analisis del número de muertes en un pais')
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()    

    else:
        print('Filtremos el pais')
        newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
        df = pd.DataFrame(newdata)
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)
        
        intxx=np.arange(0,x.size,1)
        #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        print(intxx)
        intxx = intxx[:,np.newaxis]  

        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
        x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

        poli = PolynomialFeatures(degree = 2)
        x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)

    	
        pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
        coef = pr.coef_
        print("coeficiente")
        print(coef)
        intercept = pr.intercept_
        auxy = pr.predict(x_train_polinomio)
        mse = np.sqrt(mean_squared_error(y_train_p,auxy))
        r_cuadrado = r2_score(y_train_p,auxy)
        print('r cuadrado')
        print(r_cuadrado)

        response = intercept + coef[1] * intxx+coef[2] * intxx**2  
        valoraprox = response[response.size-1]
        plt.scatter(intxx,y,color='blue')
        plt.plot(intxx,response, color='green',linewidth=3)
        plt.title('Analisis del número de muertes en ' +varpais)
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()
    
    cantidadmuertes = str(response[response.size-1])
    ecuacion = str(round(intercept,2))+'+'+ str(round(coef[1],2)) + '* x +'+ str(round(coef[2])) +'x^2'  
    print("El valor de la ecuacion es: "+str(ecuacion))
    return jsonify({"img": imagenbase64,"ecuacion":str(ecuacion),"cantidadmuertes":str(cantidadmuertes)})

@app.route('/consulta7', methods=['POST'])
def consulta7():
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
    mse=''
    r_cuadrado = ''


    if varpais == "null" or varcolpais == "null":
        print('El archivo viene sin pais')
        df = pd.DataFrame(archivoglobal)
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)

        intxx=np.arange(0,x.size,1)
        #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        print(intxx)
        intxx = intxx[:,np.newaxis]  

        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
        x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

        poli = PolynomialFeatures(degree = 2)
        x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)

    	
        pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
        coef = pr.coef_
        print("coeficiente")
        print(coef)
        intercept = pr.intercept_
        auxy = pr.predict(x_train_polinomio)
        mse = np.sqrt(mean_squared_error(y_train_p,auxy))
        r_cuadrado = r2_score(y_train_p,auxy)
        print('r cuadrado')
        print(r_cuadrado)


        response = intercept + coef[1] * intxx+coef[2] * intxx**2  
        valoraprox = response[response.size-1]
        plt.scatter(intxx,y,color='blue')
        plt.plot(intxx,response, color='green',linewidth=3)
        plt.title('Analisis del número de muertes en un pais')
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()
      

    else:
        print('Filtremos el pais')
        newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
        df = pd.DataFrame(newdata)
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)
        
        intxx=np.arange(0,x.size,1)
        #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        print(intxx)
        intxx = intxx[:,np.newaxis]  

        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
        x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

        poli = PolynomialFeatures(degree = 2)
        x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)

    	
        pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
        coef = pr.coef_
        print("coeficiente")
        print(coef)
        intercept = pr.intercept_
        auxy = pr.predict(x_train_polinomio)
        mse = np.sqrt(mean_squared_error(y_train_p,auxy))
        r_cuadrado = r2_score(y_train_p,auxy)
        print('r cuadrado')
        print(r_cuadrado)
        
        response = intercept + coef[1] * intxx+coef[2] * intxx**2  
        valoraprox = response[response.size-1]
        plt.scatter(intxx,y,color='blue')
        plt.plot(intxx,response, color='green',linewidth=3)
        plt.title('Analisis del número de muertes en ' +varpais)
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()
    

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 6))
    sns.distplot(
    y,
    hist    = False,
    rug     = True,
    color   = "blue",
    kde_kws = {'shade': True, 'linewidth': 1},
    ax      = axes
    )
    axes.set_title("Distribucion Media de infectados por dia", fontsize = 'medium')
    axes.set_xlabel(var2, fontsize='small') 
    axes.tick_params(labelsize = 6)
    plt.savefig('./reporte.png')
    with open("./reporte.png","rb") as img_file:
        imagen2base64=base64.b64encode(img_file.read())
        imagen2base64=imagen2base64.decode('utf-8')
        #print(imagenbase64)
    plt.close()
    cantidadmuertes = str(response[response.size-1])

    ecuacion = str(round(intercept,2))+'+'+ str(round(coef[1],2)) + '* x +'+ str(round(coef[2])) +'x^2'  
    print("El valor de la ecuacion es: "+str(ecuacion))
    return jsonify({"img": imagenbase64,"ecuacion":str(ecuacion),"cantidadmuertes":str(cantidadmuertes),"img2":imagen2base64})

@app.route('/consulta8', methods=['POST'])
def consulta8():
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
    
    mse=''
    r_cuadrado = ''

    if varpais == "null" or varcolpais == "null":
        print('El archivo viene sin pais')
        df = pd.DataFrame(archivoglobal)
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)
        
        varcant = x.size + 365

        intxx=np.arange(0,x.size,1)
        #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        print(intxx)
        primerdato = intxx[0]
        ultimo= intxx[intxx.size-1]
        cantidadmas = ultimo + int(varcant)
        print('Ultimo dato ='+ str(ultimo))
        intxx = intxx[:,np.newaxis]  

        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
        x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

        poli = PolynomialFeatures(degree = 2)
        x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)
    	
        pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
        coef = pr.coef_
        print("coeficiente")
        print(coef)
        intercept = pr.intercept_
        auxy = pr.predict(x_train_polinomio)
        mse = np.sqrt(mean_squared_error(y_train_p,auxy))
        r_cuadrado = r2_score(y_train_p,auxy)
        print('r cuadrado')
        print(r_cuadrado)

        nuevo_x = np.arange(primerdato,varcant,1)  #ACA CREO MI NUEVO X                          #lo convierto
        print(nuevo_x)
        print("tamanio"+str(nuevo_x.size))

        response = intercept + coef[1] * nuevo_x+coef[2] * nuevo_x**2  
        valoraprox = response[response.size-1]
        plt.scatter(intxx,y,color='blue')
        plt.plot(nuevo_x,response, color='green',linewidth=3)
        plt.title('Tendecia por Covid-19 en un pais\nLa prediccion del dia '+str(cantidadmas)+' = '+str(valoraprox))
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()

    else:
        print('Filtremos el pais')
        newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
        df = pd.DataFrame(newdata)
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)
        
        varcant = x.size + 365
        intxx=np.arange(0,x.size,1)
        #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        print(intxx)
        primerdato = intxx[0]
        ultimo= intxx[intxx.size-1]
        cantidadmas = ultimo + int(varcant)
        print('Ultimo dato ='+ str(ultimo))
        intxx = intxx[:,np.newaxis]  

        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
        x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

        poli = PolynomialFeatures(degree = 2)
        x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)


        pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
        coef = pr.coef_
        print("coeficiente")
        print(coef)
        intercept = pr.intercept_
        auxy = pr.predict(x_train_polinomio)
        mse = np.sqrt(mean_squared_error(y_train_p,auxy))
        r_cuadrado = r2_score(y_train_p,auxy)
        print('r cuadrado')
        print(r_cuadrado)

        nuevo_x = np.arange(primerdato,cantidadmas,1)  #ACA CREO MI NUEVO X                          #lo convierto
        print(nuevo_x)
        print("tamanio"+str(nuevo_x.size))

        response = intercept + coef[1] * nuevo_x+coef[2] * nuevo_x**2  
        valoraprox = response[response.size-1]
        plt.scatter(intxx,y,color='blue')
        plt.plot(nuevo_x,response, color='green',linewidth=3)
        plt.title('Tendecia por Covid-19 en '+varpais+'\nLa prediccion del dia '+str(cantidadmas)+' = '+str(round(valoraprox)))
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()

    ecuacion = str(intercept)+'+'+ str(coef[1]) + '* x +'+ str(coef[2]) +'x^2'  
    print("El valor de la ecuacion es: "+str(ecuacion))
    return jsonify({"img": imagenbase64,"mse":str(ecuacion),"val_r_cuadrado":str(r_cuadrado)})

@app.route('/consulta9', methods=['POST'])
def consulta9():
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
    mse=''
    r_cuadrado = ''


    if varpais == "null" or varcolpais == "null":
        print('El archivo viene sin pais')
        df = pd.DataFrame(archivoglobal)
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)

        intxx=np.arange(0,x.size,1)
        #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        print(intxx)
        intxx = intxx[:,np.newaxis]  

        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
        x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

        poli = PolynomialFeatures(degree = 2)
        x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)

    	
        pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
        coef = pr.coef_
        print("coeficiente")
        print(coef)
        intercept = pr.intercept_
        auxy = pr.predict(x_train_polinomio)
        mse = np.sqrt(mean_squared_error(y_train_p,auxy))
        r_cuadrado = r2_score(y_train_p,auxy)
        print('r cuadrado')
        print(r_cuadrado)


        response = intercept + coef[1] * intxx+coef[2] * intxx**2  
        valoraprox = response[response.size-1]
        plt.scatter(intxx,y,color='blue')
        plt.plot(intxx,response, color='green',linewidth=3)
        plt.title('Analisis del número de infectados en un pais')
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()
      

    else:
        print('Filtremos el pais')
        newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
        df = pd.DataFrame(newdata)
        x = df[var1].fillna(0)
        y = df[var2].fillna(0)
        
        intxx=np.arange(0,x.size,1)
        #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
        print(intxx)
        intxx = intxx[:,np.newaxis]  

        x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
        x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

        poli = PolynomialFeatures(degree = 2)
        x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)

    	
        pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
        coef = pr.coef_
        print("coeficiente")
        print(coef)
        intercept = pr.intercept_
        auxy = pr.predict(x_train_polinomio)
        mse = np.sqrt(mean_squared_error(y_train_p,auxy))
        r_cuadrado = r2_score(y_train_p,auxy)
        print('r cuadrado')
        print(r_cuadrado)
        
        response = intercept + coef[1] * intxx+coef[2] * intxx**2  
        valoraprox = response[response.size-1]
        plt.scatter(intxx,y,color='blue')
        plt.plot(intxx,response, color='green',linewidth=3)
        plt.title('Analisis del número de muertes en ' +varpais)
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        #print(imagenbase64)
        plt.close()
    
    cantidadmuertes = str(response[response.size-1])
    ecuacion = str(round(intercept,2))+'+'+ str(round(coef[1],2)) + '* x +'+ str(round(coef[2])) +'x^2'    
    print("El valor de la ecuacion es: "+str(ecuacion))
    return jsonify({"img": imagenbase64,"ecuacion":str(ecuacion),"mse":str(mse),"r_cuadrado":r_cuadrado})

@app.route('/consulta10', methods=['POST'])
def consulta10():
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
        "varpais2":datos['varpais2'],
        "variable1": datos['variable1'],
        "variable2": datos['variable2'],
        "variable3": datos['variable3'],
        "variable4": datos['variable4'],
    }
    global archivoglobal
    varcolpais = variables['varcolpais']
    varpais = variables['varpais']
    varpais2 = variables['varpais2']
    var1 = variables['variable1']
    var2 = variables['variable2']
    var3 = variables['variable3']
    var4 = variables['variable4']

    print(varcolpais)
    print(varpais)
    print(varpais2)
    print(var1)
    print(var2)
    print(var3)
    print(var4)

    mse=''
    mse2=''
    r_cuadrado = ''
    r_cuadrado2 = ''

    #---------------------------------------------------------------
    #---------------------- PARA EL PRIMER PAIS---------------------

    archivoglobal2 = archivoglobal
    print('Filtremos el pais')
    newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
    df = pd.DataFrame(newdata)
    x = df[var1].fillna(0)
    y = df[var2].fillna(0)
    
    intxx=np.arange(0,x.size,1)
    #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
    print(intxx)
    intxx = intxx[:,np.newaxis]  

    x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
    x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

    poli = PolynomialFeatures(degree = 2)
    x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)

    
    pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
    coef = pr.coef_
    print("coeficiente")
    print(coef)
    intercept = pr.intercept_
    auxy = pr.predict(x_train_polinomio)
    mse = np.sqrt(mean_squared_error(y_train_p,auxy))
    r_cuadrado = r2_score(y_train_p,auxy)
    print('r cuadrado')
    print(r_cuadrado)
    
    response = intercept + coef[1] * intxx+coef[2] * intxx**2  
    valoraprox = response[response.size-1]
    #plt.scatter(intxx,y,color='blue')
    plt.plot(intxx,response, color='green',linewidth=3)
    ecuacion = str(intercept)+'+'+ str(round(coef[1],2)) + '* x +'+ str(round(coef[2],2)) +'x^2'  
    print("El valor de la ecuacion es: "+str(ecuacion))


    #---------------------------------------------------------------
    #---------------------- PARA EL SEGUNDO PAIS---------------------

    print('Filtremos el pais')
    print(archivoglobal2)
    newdata2 = archivoglobal2.loc[archivoglobal2[varcolpais]==varpais2,:]
    df2 = pd.DataFrame(newdata2)
    x2 = df2[var3].fillna(0)
    y2 = df2[var4].fillna(0)
    
    intxx2=np.arange(0,x2.size,1)
    #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
    print(intxx2)
    intxx2 = intxx2[:,np.newaxis]  
 
    x_train_p2,x_test_p2,y_train_p2,y_test_p2 = train_test_split(intxx2,y2)
    x_train_df2, x_test_df2 = pd.DataFrame(x_train_p2), pd.DataFrame(x_test_p2)

    poli = PolynomialFeatures(degree = 2)
    x_train_polinomio2, x_test_polinomio2 = poli.fit_transform(x_train_df2), poli.fit_transform(x_test_df2)

    pr = linear_model.LinearRegression().fit(x_train_polinomio2,y_train_p2)
    coef2 = pr.coef_
    print("coeficiente")
    print(coef2)
    intercept2 = pr.intercept_
    auxy2 = pr.predict(x_train_polinomio2)
    mse2 = np.sqrt(mean_squared_error(y_train_p2,auxy2))
    r_cuadrado2 = r2_score(y_train_p2,auxy2)
    print('r cuadrado')
    print(r_cuadrado2)
    
    response2 = intercept + coef2[1] * intxx2+coef2[2] * intxx2**2  
    valoraprox = response2[response2.size-1]
    #plt.scatter(intxx,y,color='blue')
    plt.plot(intxx2,response2, color='red',linewidth=3)
    plt.title('Ánalisis Comparativo de Vacunación entre ' +varpais+' y '+varpais2)
    plt.xlabel(var1)
    plt.ylabel(var2)
    #plt.show()
    plt.savefig('./reporte.png')
    with open("./reporte.png","rb") as img_file:
        imagenbase64=base64.b64encode(img_file.read())
        imagenbase64=imagenbase64.decode('utf-8')
    #print(imagenbase64)
    plt.close()

    #cantidadmuertes = str(response[response.size-1])
    ecuacion2 = str(intercept2)+'+'+ str(round(coef2[1],2)) + '* x +'+ str(round(coef2[2],2)) +'x^2'  
    print("El valor de la ecuacion es: "+str(ecuacion2))
    return jsonify({"img": imagenbase64,"ecuacion":str(ecuacion),"mse":str(mse),"r_cuadrado":r_cuadrado
                    ,"ecuacion2":str(ecuacion2),"mse2":str(mse2),"r_cuadrado2":r_cuadrado2})

@app.route('/consulta11', methods=['POST'])
def consulta11():
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
        "vargenero": datos['vargenero'],
        "namegenero": datos['namegenero'],
    }
    global archivoglobal
    varcolpais = variables['varcolpais']
    varpais = variables['varpais']
    var1 = variables['variable1']
    var2 = variables['variable2']
    var3 = variables['vargenero']
    name = variables['namegenero']

    if name == '':
        name = "Hombre"
    

    print(varcolpais)
    print(varpais)
    print(var1)
    print(var2)
    print(var3)

    print('Filtremos el pais')
    newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
    dff = pd.DataFrame(newdata)
    auxx = dff[var1].fillna(0)
    auxy = dff[var2].fillna(0)
    
    newdata2 = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
    newdata2 = newdata2.loc[archivoglobal[var3]==name,:]

    df = pd.DataFrame(newdata2)
    x = df[var1]
    y = df[var2]
    varcant = 0

    for a in y:
        varcant += 1
    
    porcentaje = varcant / auxy.size

    plt.scatter(auxx, auxy,color ='green')
    plt.scatter(x,y,color='blue')
    plt.title('Porcentaje de hombres infectados por covid-19 en ' +varpais+'\ndesde el primer caso activo.\nPoblacion general(Verde) vs. Hombres(Azul)')
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.savefig('./reporte.png')
    with open("./reporte.png","rb") as img_file:
        imagenbase64=base64.b64encode(img_file.read())
        imagenbase64=imagenbase64.decode('utf-8')
    plt.close()

    return jsonify({"img":imagenbase64,"porcentaje":str(round(porcentaje*100,2)),"total":str(auxy.size),'hombres':str(varcant)})



@app.route('/consulta13', methods=['POST'])
def consulta13():
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
        "variable3": datos['variable3'],
    }
    global archivoglobal
    varcolpais = variables['varcolpais']
    varpais = variables['varpais']
    var1 = variables['variable1']
    var2 = variables['variable2']
    var3 = variables['variable3']
    

    print(varcolpais)
    print(varpais)
    print(var1)
    print(var2)
    print(var3)

    print('Filtremos el pais')
    newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
    dff = pd.DataFrame(newdata)
    auxx = dff[var2].fillna(0)
    auxy = dff[var1].fillna(0)
    x = dff[var3].fillna(0)
 

    plt.scatter(auxx, auxy,color ='green')
    plt.title('Casos confirmados vs Muertes promedio de ' +varpais)
    plt.xlabel(var2)
    plt.ylabel(var1)
    plt.savefig('./reporte.png')
    with open("./reporte.png","rb") as img_file:
        imagenbase64=base64.b64encode(img_file.read())
        imagenbase64=imagenbase64.decode('utf-8')
    plt.close()


    plt.scatter(x, auxy,color ='blue')
    plt.title('edad vs Muertes promedio de ' +varpais)
    plt.xlabel(var3)
    plt.ylabel(var1)
    plt.savefig('./reporte2.png')
    with open("./reporte2.png","rb") as img_file:
        imagen2base64=base64.b64encode(img_file.read())
        imagen2base64=imagen2base64.decode('utf-8')
    plt.close()

    return jsonify({"img":imagenbase64,"img2":imagen2base64,"promedio":str(auxy.mean())})

@app.route('/consulta14', methods=['POST'])
def consulta14():
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
    
    print('Filtremos el pais')
    newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]    
    df = pd.DataFrame(newdata)
    dff = df.groupby([var1]).sum().reset_index()
    
    print(dff)
    x = dff[var1].fillna(0)
    y = dff[var2].fillna(0)

    plt.bar(x, y,color ='blue',linestyle="-", label="Muertes")
    plt.title('Muertes segun la region de ' +varpais)
    plt.xlabel(var1,fontdict = {'fontsize':3})
    plt.ylabel(var2)
    plt.savefig('./reporte.png')
    with open("./reporte.png","rb") as img_file:
        imagenbase64=base64.b64encode(img_file.read())
        imagenbase64=imagenbase64.decode('utf-8')
    plt.close()
    return jsonify({"img":imagenbase64})

@app.route('/consulta15', methods=['POST'])
def consulta15():
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
        "varcoldep":datos['varcoldep'],
        "vardep":datos['vardep'],
        "variable1": datos['variable1'],
        "variable2": datos['variable2'],
    }
    global archivoglobal
    varcolpais = variables['varcolpais']
    varpais = variables['varpais']
    varcoldep = variables['varcoldep']
    vardep = variables['vardep']
    var1 = variables['variable1']
    var2 = variables['variable2']
    mse=''
    r_cuadrado = ''

    print('Filtremos el pais')
    newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
    newdata = newdata.loc[archivoglobal[varcoldep]==vardep,:]
    df = pd.DataFrame(newdata)
    x = df[var1].fillna(0)
    y = df[var2].fillna(0)
    
    intxx=np.arange(0,x.size,1)
    #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
    print(intxx)
    intxx = intxx[:,np.newaxis]  

    x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
    x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

    poli = PolynomialFeatures(degree = 2)
    x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)

    
    pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
    coef = pr.coef_
    print("coeficiente")
    print(coef)
    intercept = pr.intercept_
    auxy = pr.predict(x_train_polinomio)
    mse = np.sqrt(mean_squared_error(y_train_p,auxy))
    r_cuadrado = r2_score(y_train_p,auxy)
    print('r cuadrado')
    print(r_cuadrado)
    
    response = intercept + coef[1] * intxx+coef[2] * intxx**2  
    valoraprox = response[response.size-1]
    plt.scatter(intxx,y,color='blue')
    plt.plot(intxx,response, color='green',linewidth=3)
    plt.title('Analisis del número de muertes en ' +varpais)
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.savefig('./reporte.png')
    with open("./reporte.png","rb") as img_file:
        imagenbase64=base64.b64encode(img_file.read())
        imagenbase64=imagenbase64.decode('utf-8')
    #print(imagenbase64)
    plt.close()
    
    cantidadmuertes = str(response[response.size-1])
    ecuacion = str(intercept)+'+'+ str(round(coef[1],2)) + '* x +'+ str(round(coef[2],2)) +'x^2'  
    print("El valor de la ecuacion es: "+str(ecuacion))
    return jsonify({"img": imagenbase64,"ecuacion":str(ecuacion),"mse":str(mse),"r_cuadrado":r_cuadrado})

@app.route('/consulta16', methods=['POST'])
def consulta16():
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
        "vargenero": datos['vargenero'],
        "namegenero": datos['namegenero'],
    }
    global archivoglobal
    varcolpais = variables['varcolpais']
    varpais = variables['varpais']
    var1 = variables['variable1']
    var2 = variables['variable2']
    var3 = variables['vargenero']
    name = variables['namegenero']

    if name == '':
        name = "Mujer"
    

    print(varcolpais)
    print(varpais)
    print(var1)
    print(var2)
    print(var3)

    print('Filtremos el pais')
    newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
    dff = pd.DataFrame(newdata)
    auxx = dff[var1].fillna(0)
    auxy = dff[var2].fillna(0)
    
    newdata2 = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
    newdata2 = newdata2.loc[archivoglobal[var3]==name,:]

    df = pd.DataFrame(newdata2)
    x = df[var1].fillna(0)
    y = df[var2].fillna(0)
    varcant = 0

    for a in y:
        varcant += 1
    
    porcentaje = varcant / auxy.size

    plt.scatter(auxx, auxy,color ='green',label="Total" )
    plt.scatter(x,y,color='pink',label="Mujeres")
    plt.title('Porcentaje de mujeres infectados por covid-19 en ' +varpais+'\n frente al total de casos en un país, región o continente.')
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.savefig('./reporte.png')
    with open("./reporte.png","rb") as img_file:
        imagenbase64=base64.b64encode(img_file.read())
        imagenbase64=imagenbase64.decode('utf-8')
    plt.close()

    return jsonify({"img":imagenbase64,"porcentaje":str(round(porcentaje*100,2)),"total":str(auxy.size),'hombres':str(varcant)})

@app.route('/consulta17', methods=['POST'])
def consulta17():
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
        "variable3": datos['variable3'],
    }
    global archivoglobal
    varcolpais = variables['varcolpais']
    varpais = variables['varpais']
    var1 = variables['variable1']
    var2 = variables['variable2']
    var3 = variables['variable3']
    
    print('Filtremos el continente')
    newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]    
    df = pd.DataFrame(newdata)

    tablamuertes = df[var2].fillna(0)
    tablainfectados = df[var3].fillna(0)

    tablaresultado = tablamuertes/tablainfectados

    x = df[var1].fillna(0)

    plt.plot(x, tablaresultado,color ='blue',linestyle="-", label="Muertes")
    plt.title('Tasa de comportamiento de casos activos en relacion al numero\nde muertes en el continente ' +varpais)
    plt.xlabel(var1)
    plt.ylabel('Tasa de comportamiento')
    plt.savefig('./reporte.png')
    with open("./reporte.png","rb") as img_file:
        imagenbase64=base64.b64encode(img_file.read())
        imagenbase64=imagenbase64.decode('utf-8')
    plt.close()

    tasa = str(round(tablaresultado.mean(),2))
    return jsonify({"img":imagenbase64, "tasa":tasa})

@app.route('/consulta18', methods=['POST'])
def consulta18():
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
        "varcolmuni":datos['varcolmuni'],
        "varmuni":datos['varmuni'],
        "variable1": datos['variable1'],
        "variable2": datos['variable2'],
    }
    global archivoglobal
    varcolpais = variables['varcolpais']
    varpais = variables['varpais']
    varcolmuni = variables['varcolmuni']
    varmuni = variables['varmuni']
    var1 = variables['variable1']
    var2 = variables['variable2']


    print('Filtremos el pais')
    newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
    newdata = newdata.loc[archivoglobal[varcolmuni]==varmuni,:]
    
    df = pd.DataFrame(newdata)
    x = df[var1].fillna(0)
    y = df[var2].fillna(0)
    
    plt.scatter(x,y,color ='orange',linestyle="-", label="Muertes")
    plt.title('Tasa de comportamiento de casos activos en relacion al numero\nde muertes en el continente ' +varpais)
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.savefig('./reporte.png')
    with open("./reporte.png","rb") as img_file:
        imagenbase64=base64.b64encode(img_file.read())
        imagenbase64=imagenbase64.decode('utf-8')
    plt.close()
    return jsonify({"img": imagenbase64})

@app.route('/consulta19', methods=['POST'])
def consulta19():
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
    
    mse=''
    r_cuadrado = ''    

    print('Filtremos el pais')
    newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
    df = pd.DataFrame(newdata)
    x = df[var1].fillna(0)
    y = df[var2].fillna(0)
    
    varcant = x.size + 365
    intxx=np.arange(0,x.size,1)
    #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
    print(intxx)
    primerdato = intxx[0]
    ultimo= intxx[intxx.size-1]
    cantidadmas = ultimo + int(varcant)
    print('Ultimo dato ='+ str(ultimo))
    intxx = intxx[:,np.newaxis]  

    x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
    x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

    poli = PolynomialFeatures(degree = 2)
    x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)


    pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
    coef = pr.coef_
    print("coeficiente")
    print(coef)
    intercept = pr.intercept_
    auxy = pr.predict(x_train_polinomio)
    mse = np.sqrt(mean_squared_error(y_train_p,auxy))
    r_cuadrado = r2_score(y_train_p,auxy)
    print('r cuadrado')
    print(r_cuadrado)

    nuevo_x = np.arange(primerdato,varcant,1)  #ACA CREO MI NUEVO X                          #lo convierto
    print(nuevo_x)
    print("tamanio"+str(nuevo_x.size))

    response = intercept + coef[1] * nuevo_x+coef[2] * nuevo_x**2  
    valoraprox = response[response.size-1]

    plt.scatter(intxx,y,color='blue')
    plt.plot(nuevo_x,response, color='green',linewidth=3)
    plt.title('Tendecia por Covid-19 en '+varpais+'\nLa prediccion del dia '+str(nuevo_x.size)+' = '+str(round(valoraprox)))
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.savefig('./reporte.png')
    with open("./reporte.png","rb") as img_file:
        imagenbase64=base64.b64encode(img_file.read())
        imagenbase64=imagenbase64.decode('utf-8')
    #print(imagenbase64)
    plt.close()

    ecuacion = str(round(intercept,2))+'+'+ str(round(coef[1],2)) + '* x +'+ str(round(coef[2],2)) +'x^2'  
    print("El valor de la ecuacion es: "+str(ecuacion))
    return jsonify({"img": imagenbase64,"mse":str(ecuacion),"val_r_cuadrado":str(round(r_cuadrado,2)),"aprox":str(round(valoraprox))})
    #return jsonify({"img": "hola"})

@app.route('/consulta20', methods=['POST'])
def consulta20():
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
        "variable3": datos['variable3'],
    }
    global archivoglobal
    varcolpais = variables['varcolpais']
    varpais = variables['varpais']
    var1 = variables['variable1']
    var2 = variables['variable2']
    var3 = variables['variable3']
    
    if varcolpais == '' or varpais == '':
        print('Filtremos el continente')       
        df = pd.DataFrame(archivoglobal)

        tablainfecdiarios = df[var3].fillna(0)
        tablainfectados = df[var1].fillna(0)

        tablaresultado = tablainfecdiarios/tablainfectados *100
        x = df[var1].fillna(0)

        plt.plot(x, tablaresultado,color ='blue',linestyle="-", label="Muertes")
        plt.title('Tasa de crecimiento de casos de COVID-19 en relación con nuevos casos\ndiarios en ' +varpais)
        plt.xlabel(var1)
        plt.ylabel('Tasa de crecimiento')
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        plt.close()

        tablamuertes = df[var2].fillna(0)
        tablaresultado2 = tablamuertes/tablainfectados*100
        print(tablaresultado2)
        plt.plot(x, tablaresultado2,color ='red',linestyle="-", label="Muertes")
        plt.title('Tasa de mortalidad por COVID-19 en ' +varpais)
        plt.xlabel(var1)
        plt.ylabel('Tasa de mortalidad')
        plt.savefig('./reporte2.png')
        with open("./reporte2.png","rb") as img_file:
            imagen2base64=base64.b64encode(img_file.read())
            imagen2base64=imagen2base64.decode('utf-8')
        plt.close()

    else:
        print('Filtremos el continente')
        newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]    
        df = pd.DataFrame(newdata)

        tablainfecdiarios = df[var3].fillna(0)
        tablainfectados = df[var1].fillna(0)

        tablaresultado = tablainfecdiarios/tablainfectados *100
        x = df[var1].fillna(0)

        plt.plot(x, tablaresultado,color ='blue',linestyle="-", label="Muertes")
        plt.title('Tasa de crecimiento de casos de COVID-19 en relación con nuevos casos\ndiarios en ' +varpais)
        plt.xlabel(var1)
        plt.ylabel('Tasa de crecimiento')
        plt.savefig('./reporte.png')
        with open("./reporte.png","rb") as img_file:
            imagenbase64=base64.b64encode(img_file.read())
            imagenbase64=imagenbase64.decode('utf-8')
        plt.close()

        tablamuertes = df[var2].fillna(0)
        tablaresultado2 = tablamuertes/tablainfectados*100
        print(tablaresultado2)
        plt.plot(x, tablaresultado2,color ='red',linestyle="-", label="Muertes")
        plt.title('Tasa de mortalidad por COVID-19 en ' +varpais)
        plt.xlabel(var1)
        plt.ylabel('Tasa de mortalidad')
        plt.savefig('./reporte2.png')
        with open("./reporte2.png","rb") as img_file:
            imagen2base64=base64.b64encode(img_file.read())
            imagen2base64=imagen2base64.decode('utf-8')
        plt.close()

    tasa = str(round(tablaresultado.mean(),2))
    tasa2 = str(round(tablaresultado2.mean(),2))

    return jsonify({"img":imagenbase64, "tasa":tasa,"img2":imagen2base64, "tasa2":tasa2})

@app.route('/consulta21', methods=['POST'])
def consulta21():
    print("Hola mundo\n\n\n")
    datos=""
    datos = request.get_data()
    print(datos)
    datos=datos.decode('utf-8')
    datos = json.loads(datos)
    print(datos)

    variables = {
        "variable1": datos['variable1'],
        "variable2": datos['variable2'],
        "variable3": datos['variable3'],
        "cant": datos['cant'],
    }

    var1 = variables['variable1']
    var2 = variables['variable2']
    var3 = variables['variable3']
    cant = variables['cant']
    
    mse=''
    r_cuadrado = ''    

    print('Filtremos el pais')
    df = pd.DataFrame(archivoglobal)
    x = df[var1].fillna(0)
    y = df[var2].fillna(0)
    y2= df[var3].fillna(0)
    
    varcant =  int(cant)
    intxx=np.arange(0,x.size,1)
    #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
    print(intxx)
    primerdato = intxx[0]
    ultimo= intxx[intxx.size-1]
    cantidadmas = intxx.size + int(cant)
    print('Ultimo dato ='+ str(ultimo))
    intxx = intxx[:,np.newaxis]  

    x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
    x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

    poli = PolynomialFeatures(degree = 2)
    x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)


    pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
    coef = pr.coef_
    print("coeficiente")
    print(coef)
    intercept = pr.intercept_
    auxy = pr.predict(x_train_polinomio)
    mse = np.sqrt(mean_squared_error(y_train_p,auxy))
    r_cuadrado = r2_score(y_train_p,auxy)
    print('r cuadrado')
    print(r_cuadrado)

    nuevo_x = np.arange(primerdato,cantidadmas,1)  #ACA CREO MI NUEVO X                          #lo convierto
    print(nuevo_x)
    print("tamanio"+str(nuevo_x.size))

    response = intercept + coef[1] * nuevo_x+coef[2] * nuevo_x**2  
    valoraprox = response[response.size-1]

    plt.scatter(intxx,y,color='blue')
    plt.plot(nuevo_x,response, color='green',linewidth=3)
    plt.title('Prediccion de Casos en todo el mundo\nNeural Network MLPRegressor  '+str(cantidadmas)+' = '+str(round(valoraprox)))
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.savefig('./reporte.png')
    with open("./reporte.png","rb") as img_file:
        imagenbase64=base64.b64encode(img_file.read())
        imagenbase64=imagenbase64.decode('utf-8')
    #print(imagenbase64)
    plt.close()

    #----------------------------------------------------------
    #-------------- otro

    x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y2)
    x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

    poli = PolynomialFeatures(degree = 2)
    x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)


    pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
    coef2 = pr.coef_
    print("coeficiente")
    print(coef)
    intercept2 = pr.intercept_
    auxy = pr.predict(x_train_polinomio)
    mse = np.sqrt(mean_squared_error(y_train_p,auxy))
    r_cuadrado2 = r2_score(y_train_p,auxy)
    print('r cuadrado')
    print(r_cuadrado2)

    nuevo_x = np.arange(primerdato,cantidadmas,1)  #ACA CREO MI NUEVO X                          #lo convierto
    print(nuevo_x)
    print("tamanio"+str(nuevo_x.size))

    response = intercept2 + coef2[1] * nuevo_x+coef2[2] * nuevo_x**2  
    valoraprox2 = response[response.size-1]

    plt.scatter(intxx,y2,color='red')
    plt.plot(nuevo_x,response, color='black',linewidth=3)
    plt.title('Prediccion de muertes en todo el mundo\nNeural Network MLPRegressor  '+str(cantidadmas)+' = '+str(round(valoraprox2)))
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.savefig('./reporte2.png')
    with open("./reporte2.png","rb") as img_file:
        imagen2base64=base64.b64encode(img_file.read())
        imagen2base64=imagen2base64.decode('utf-8')
    #print(imagenbase64)
    plt.close()

    ecuacion = str(round(intercept,2))+'+'+ str(round(coef[1],2)) + '* x +'+ str(round(coef[2],2)) +'x^2'  
    ecuacion2 = str(round(intercept2,2))+'+'+ str(round(coef2[1],2)) + '* x +'+ str(round(coef2[2],2)) +'x^2'  
    print("El valor de la ecuacion es: "+str(ecuacion))


    return jsonify({"img": imagenbase64,"mse":str(ecuacion),"val_r_cuadrado":str(round(r_cuadrado,2)),"aprox":str(round(valoraprox))
                    ,"img2": imagen2base64,"mse2":str(ecuacion2),"val_r_cuadrado2":str(round(r_cuadrado2,2)),"aprox2":str(round(valoraprox2))})
    #return jsonify({"img": "hola"})

@app.route('/consulta22', methods=['POST'])
def consulta22():
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
        "variable3": datos['variable3'],
    }
    global archivoglobal
    varcolpais = variables['varcolpais']
    varpais = variables['varpais']
    var1 = variables['variable1']
    var2 = variables['variable2']
    var3 = variables['variable3']
    
    print('Filtremos el continente')
    newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]    
    df = pd.DataFrame(newdata)

    tablamuertes = df[var2].fillna(0)
    tablainfectados = df[var3].fillna(0)

    tablaresultado = tablamuertes/tablainfectados

    x = df[var1].fillna(0)

    plt.plot(x, tablaresultado,color ='red',linestyle="-", label="Muertes")
    plt.title('Tasa de mortalidad por coronavirus (COVID-19) en el pais ' +varpais)
    plt.xlabel(var1)
    plt.ylabel('Tasa de comportamiento')
    plt.savefig('./reporte.png')
    with open("./reporte.png","rb") as img_file:
        imagenbase64=base64.b64encode(img_file.read())
        imagenbase64=imagenbase64.decode('utf-8')
    plt.close()

    tasa = str(round(tablaresultado.mean(),2))
    return jsonify({"img":imagenbase64, "tasa":tasa})

@app.route('/consulta23', methods=['POST'])
def consulta23():
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
    
    print('Filtremos el pais')
    newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]    
    df = pd.DataFrame(newdata)
    dff = df.groupby([var2]).sum().reset_index()
    
    print(dff)
    x = dff[var2].fillna(0)
    y = dff[var1].fillna(0)

    plt.bar(x, y,color ='blue',linestyle="-", label="Muertes")
    plt.title('Factores de muerte por COVID-19 en ' +varpais)
    plt.xlabel(var2)
    plt.ylabel(var1)
    plt.savefig('./reporte.png')
    with open("./reporte.png","rb") as img_file:
        imagenbase64=base64.b64encode(img_file.read())
        imagenbase64=imagenbase64.decode('utf-8')
    plt.close()
    return jsonify({"img":imagenbase64})

@app.route('/consulta24', methods=['POST'])
def consulta24():
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
        "variable3": datos['variable3'],
    }
    global archivoglobal
    varcolpais = variables['varcolpais']
    varpais = variables['varpais']
    var1 = variables['variable1']
    var2 = variables['variable2']
    var3 = variables['variable3']
    
    print('Filtremos el pais')
    newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]    
    df = pd.DataFrame(newdata)
    
    print(df)
    x = df[var1].fillna(0)
    y = df[var2].fillna(0)
    y2 = df[var3].fillna(0)

    cantidadinfec=y.sum()
    cantidadvacunas =y2.sum()

    conclusion=''

    if cantidadinfec>cantidadvacunas:
        conclusion = 'Como se puede obserbar en el grafico la cantidad de infectados\nes mayor a la cantidad de personas vacunadas por ende se\nrecomienda incrementar las medidas de vacunacion en el pais.'
    else:
        conclusion = 'Como se puede obserbar en el grafico la cantidad de infectados\nes menor a la cantida de personas vacunadas con esto podemos\nconcluir que la pandemia en ese pais esta disminuyendo devido al\nexcelente manejo de vacuancion del pais.'
        

    plt.plot(x, y,color ='blue',linestyle="-", label="Muertes")
    plt.plot(x, y2,color ='orange',linestyle="-", label="Muertes")
    plt.title('Comparación entre el número de casos detectados(Azul)\ny el número de pruebas de un país(Naranja).' +varpais)
    plt.xlabel(var1)
    plt.ylabel('Casos detectados y numero de pruebas')
    plt.savefig('./reporte.png')
    with open("./reporte.png","rb") as img_file:
        imagenbase64=base64.b64encode(img_file.read())
        imagenbase64=imagenbase64.decode('utf-8')
    plt.close()
    return jsonify({"img":imagenbase64,"conc":conclusion})


@app.route('/consulta25', methods=['POST'])
def consulta25():
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
        "cantidad": datos['cant'],
    }
    global archivoglobal
    varcolpais = variables['varcolpais']
    varpais = variables['varpais']
    var1 = variables['variable1']
    var2 = variables['variable2']
    cant = variables['cantidad']
    
    mse=''
    r_cuadrado = ''    

    print('Filtremos el pais')
    newdata = archivoglobal.loc[archivoglobal[varcolpais]==varpais,:]
    df = pd.DataFrame(newdata)
    x = df[var1].fillna(0)
    y = df[var2].fillna(0)
    
    varcant = x.size + int(cant)
    intxx=np.arange(0,x.size,1)
    #intxx = pd.to_datetime(x).astype(np.int64)   #CONVIERTO DE FECHAS A INT
    print(intxx)
    primerdato = intxx[0]
    ultimo= intxx[intxx.size-1]
    cantidadmas = ultimo + int(cant)
    print('Ultimo dato ='+ str(ultimo))
    intxx = intxx[:,np.newaxis]  

    x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(intxx,y)
    x_train_df, x_test_df = pd.DataFrame(x_train_p), pd.DataFrame(x_test_p)

    poli = PolynomialFeatures(degree = 2)
    x_train_polinomio, x_test_polinomio = poli.fit_transform(x_train_df), poli.fit_transform(x_test_df)


    pr = linear_model.LinearRegression().fit(x_train_polinomio,y_train_p)
    coef = pr.coef_
    print("coeficiente")
    print(coef)
    intercept = pr.intercept_
    auxy = pr.predict(x_train_polinomio)
    mse = np.sqrt(mean_squared_error(y_train_p,auxy))
    r_cuadrado = r2_score(y_train_p,auxy)
    print('r cuadrado')
    print(r_cuadrado)

    nuevo_x = np.arange(primerdato,varcant,1)  #ACA CREO MI NUEVO X                          #lo convierto
    print(nuevo_x)
    print("tamanio"+str(nuevo_x.size))

    response = intercept + coef[1] * nuevo_x+coef[2] * nuevo_x**2  
    valoraprox = response[response.size-1]

    plt.scatter(intxx,y,color='blue')
    plt.plot(nuevo_x,response, color='green',linewidth=3)
    plt.title('Tendecia por Covid-19 en '+varpais+'\nLa prediccion del dia '+str(cantidadmas)+' = '+str(round(valoraprox)))
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.savefig('./reporte.png')
    with open("./reporte.png","rb") as img_file:
        imagenbase64=base64.b64encode(img_file.read())
        imagenbase64=imagenbase64.decode('utf-8')
    #print(imagenbase64)
    plt.close()

    ecuacion = str(round(intercept,2))+'+'+ str(round(coef[1],2)) + '* x +'+ str(round(coef[2],2)) +'x^2'  
    print("El valor de la ecuacion es: "+str(ecuacion))
    return jsonify({"img": imagenbase64,"mse":str(ecuacion),"val_r_cuadrado":str(round(r_cuadrado,2)),"aprox":str(round(valoraprox))})
    #return jsonify({"img": "hola"})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=4000)
