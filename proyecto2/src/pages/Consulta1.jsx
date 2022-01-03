import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import "../components/style/Consulta1.css";
import logo from "./IMG/preview.png"
import Reporte from "../components/Report/Reporte1"
import {jsPDF} from 'jspdf'
import fiusac from "./IMG/logo+fiusac.png"


const Consulta1 = (props) => {

    const [switchComp, setSwitch] = useState(false);
    const [imagenmostrar,setimg]=useState({
        img: logo,
        ecuacion: 'y= ax+b',
        val_r_cuadrado:'R^2',
        pendiente:'m'
    })
    
    
    const [datos, setDatos] = useState({
        varcolpais: '',
        varpais: '',
        variable1: '',
        variable2: '',
        //local:'hola',
    })
    const handleuserchange = (event) =>{
        setDatos({...datos,[event.target.name]: event.target.value})
    }


    const enviarDatos = async(event) =>{
        console.log("datos:"+datos.varcolpais+"\nContrasenia:"+datos.varpais)
        setSwitch(true)
        if (datos.varcolpais == '') {
            //console.log("vacio")
            datos.varcolpais = 'null';
        }
        console.log("datos a enviar")
        console.log(datos)
        try {
            let configuracion = {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            }
            let respuesta = await fetch('http://localhost:4000/consulta1', configuracion)
            let json = await respuesta.json();
            console.log('valor de la respuesta json')
            console.log(json)
            imagenmostrar.img = "data:image/png;base64, "+json.img
            //console.log("valor de la imagen en react")
            //console.log(imagenmostrar.img)
            imagenmostrar.ecuacion = json.ecuacion
            console.log("valor de la ecuacion en react")
            console.log(imagenmostrar.ecuacion)
            imagenmostrar.val_r_cuadrado = "R^2 = "+json.val_r
            console.log("valor del coeficiente en react")
            console.log(imagenmostrar.val_r_cuadrado)

            console.log("valor de la pendiente en react")
            var varpen = "pendiente = "+json.pendiente
            //necesito analizar desde aca la pendiente
            //var varint = parseInt(json.pendiente)
            //console.log(varint)
            varpen >= 0.7 ?  imagenmostrar.pendiente='Se puede observar que el modelo cuenta con una tendencia negativa,\ncon una presicion del modelo de'+ json.pendiente+',\nesto quiere decir que a medida que el valor de X aumenta, el valor\nde y disminuye. Por tanto se puede conluir que la la infeccion de\nCOVID-19 disminuira con el paso del tiempo.' : imagenmostrar.pendiente='Se puede observar que el modelo cuenta con una tendencia positiva,\nesto quiere decir que a medida que el valor de X aumenta, el valor\nde y tambien aumenta. Por tanto se puede conluir que la la infeccion\nde COVID-19 aumentara con el paso del tiempo.'
            //console.log(imagenmostrar.pendiente)
        } catch (error) {

        }
    }

    function descargar(){
        var doc = new jsPDF('p', 'pt');
        doc.setFont('Comic Sans','italic')
        doc.text(20, 20, 'Universidad San Calos de Guatemala\nFacultad de Ingenieria\nEscuela de Ciencias y Sistemas\nOLC2')
  
        doc.setFont('Arial', 'normal')
        doc.text('Tendencia de la infección por Covid-19 en un País.',130,130 )
        doc.text(20, 160, 'La subregión del Caribe y el Océano Atlántico sigue viendo una aceleración \nde los casos de COVID-19, y algunos países han declarado una quinta oleada \nde la pandemia en los últimos días. Entre los 36 países y territorios de la \nsubregión, al menos la mitad de ellos han experimentado un aumento del \n100% o más de casos durante los últimos 7 días en comparación con los \n7 días anteriores (rango: 100% - 879%).')      
        doc.text(20, 300, 'Manual de aplicacion del modelo de regresion polinomial para una tendencia de\ninfeccion de COVID-19:')
        doc.addImage(imagenmostrar.img,'PNG',100,320,380,280)
        doc.addImage(fiusac,'PNG',470,10,75,75)
        doc.text(100,620,'Ecuacion del modelo de regresion polinomial de grado 2:')
        doc.setTextColor(0,0,255)
        doc.text(150,640,imagenmostrar.ecuacion)
        doc.setTextColor(0,0,0)
        doc.text(100,660,'Coeficiente de determinacion(R^2):')
        doc.setTextColor(0,0,255)
        doc.text(150,680,imagenmostrar.val_r_cuadrado)
        doc.setTextColor(50,50,50)
        doc.setTextColor(0,0,0)
        doc.text(100,700,'Conclusion de tendencia:')
        doc.setTextColor(0,0,255)
        doc.text(80,720,imagenmostrar.pendiente)
        doc.setTextColor(50,50,50)
        doc.setFont('Comic Sans','italic')
        doc.setFontSize('13')
        doc.text(355,810,'Autor: Wilfred Stewart Perez Solorzano\nCarnet:201408419')
        doc.save('demo.pdf')
    }

    function Componente(){
        if (switchComp) {
            return (
                <div>
                    <Reporte contenido={imagenmostrar} />                  
                </div>
                
            )
        }else{
            return(
                <div >
                    <br/>
                    <br/>
                    <br/><center>
                    <h1 id="id_prev_reporte">Reporte</h1>
                    </center>
                </div>
            )
        }
    }

    function verpreview(){
        setSwitch(!switchComp)
    }


    return (
        <div id="ID_general">
            <div id="ID_consulta">
                <center><h2>Tendencia de la infección por Covid-19 en un País.</h2></center>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Ingrese la columna del pais</Form.Label>
                    <Form.Control name="varcolpais" type="text" placeholder="Ingrese la columna del pais"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese el nombre del Pais</Form.Label>
                    <Form.Control name="varpais" type="text" placeholder="Ingrese el nombre del pais"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de fechas</Form.Label>
                    <Form.Control name="variable1" type="text" placeholder="Ingrese la columna de fechas"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de casos confirmados</Form.Label>
                    <Form.Control name="variable2" type="text" placeholder="Ingrese la columna de casos confirmados" onChange={handleuserchange} />
                </Form.Group>
                <Button variant="danger" id="boton_enviar" onClick={enviarDatos}>Enviar</Button>
            </div>           
            <br/>
                <Button variant="info" id="boton_enviar" onClick={verpreview}>* Preview *</Button> 
                <Componente/>

                <div id="ID_div_boton">
                <Button variant="success" id="descargar" onClick={descargar} >Descargar reporte</Button>
            </div>
            
        </div>//div global
    )

}

export default Consulta1