import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import "../components/style/Consulta1.css";
import logo from "./IMG/preview.png"
import Reporte from "../components/Report/Reporte6"
import {jsPDF} from 'jspdf'


const Consulta6 = (props) => {

    const [switchComp, setSwitch] = useState(0);
    const [imagenmostrar,setimg]=useState({
        img: logo,
        ecuacion: 'y= ax+b',
        val_r_cuadrado:'R^2',
        aproximaciones: '[1,2,3,4,5]',
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
        setSwitch(1)
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
            let respuesta = await fetch('http://localhost:4000/consulta6', configuracion)
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
            setimg({...imagenmostrar,aproximaciones : json.aproximaciones})
            console.log("valor de las aproximaciones en react")
            console.log(imagenmostrar.aproximaciones)
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
        doc.text(20, 300, 'Manual de aplicacion del modelo de regresion lineal para una tendencia de\ninfeccion de COVID-19:')
        doc.addImage(imagenmostrar.img,'PNG',100,320,380,280)
        doc.text(100,620,'Ecuacion del modelo de regresion lineal:')
        doc.setTextColor(0,0,255)
        doc.text(150,640,imagenmostrar.ecuacion)
        doc.setTextColor(0,0,0)
        doc.text(100,660,'Coeficiente de determinacion(R^2):')
        doc.setTextColor(0,0,255)
        doc.text(150,680,imagenmostrar.val_r_cuadrado)
        doc.setTextColor(0,0,0)
        doc.text(100,700,'5 Aproximaciones posteriores utilizando la ecuacion:')
        doc.setTextColor(0,0,255)
        doc.text(50,720,imagenmostrar.aproximaciones)
        doc.setTextColor(50,50,50)
        doc.setFont('Comic Sans','italic')
        doc.text(300,800,'Autor: Wilfred Stewart Perez Solorzano\nCarnet:201408419')
        doc.save('demo.pdf')
    }

    function Componente(){
        if (switchComp===1) {
            return (
                <div>
                    <Reporte contenido={imagenmostrar} />
                    <div id="ID_div_boton">
                <Button variant="success" id="descargar" onClick={descargar} >Descargar reporte</Button>
            </div>
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


    return (
        <div id="ID_general">
            <div id="ID_consulta">
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
                <Button variant="outline-info" id="boton_enviar" onClick={enviarDatos}>Enviar</Button>

            </div>
                
                <Componente/>
            
        </div>//div global
    )

}

export default Consulta6