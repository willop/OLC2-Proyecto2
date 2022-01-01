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
        x = df[var1]
        y = df[var2]

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
    ecuacion = str(pr.coef_[1])+'x+'+str(pr.coef_[2])+'x^2+'+str(pr.intercept_)
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
        x = df[var1]
        y = df[var2]

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
        x = df[var1]
        y = df[var2]
        
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
    
    ecuacion = str(intercept)+'+'+ str(coef[1]) + '* x +'+ str(coef[2]) +'x^2'  
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
        x = df[var1]
        y = df[var2]

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
        x = df[var1]
        y = df[var2]
        
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
    
    ecuacion = str(intercept)+'+'+ str(coef[1]) + '* x +'+ str(coef[2]) +'x^2'  
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
        x = df[var1]
        y = df[var2]

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
        x = df[var1]
        y = df[var2]
        
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
    
    ecuacion = str(intercept)+'+'+ str(coef[1]) + '* x +'+ str(coef[2]) +'x^2'  
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
        x = df[var1]
        y = df[var2]

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
        x = df[var1]
        y = df[var2]
        
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
    ecuacion = str(intercept)+'+'+ str(coef[1]) + '* x +'+ str(coef[2]) +'x^2'  
    print("El valor de la ecuacion es: "+str(ecuacion))
    return jsonify({"img": imagenbase64,"ecuacion":str(ecuacion),"cantidadmuertes":str(cantidadmuertes)})



if __name__ == '__main__':
    app.run(debug=True,port=4000)
