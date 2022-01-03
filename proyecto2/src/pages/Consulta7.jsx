import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import "../components/style/Consulta1.css";
import logo from "./IMG/preview.png"
import Reporte7 from "../components/Report/Reporte7"
import {jsPDF} from 'jspdf'
import fiusac from "./IMG/logo+fiusac.png"

const Consulta7 = (props) => {

    const [switchComp, setSwitch] = useState(false);
    const [imagenmostrar,setimg]=useState({
        img: logo,
        ecuacion: 'y= ax+b',
        cantidadmuertes:'',
        conclusion:''
        
    })
    
    
    const [datos, setDatos] = useState({
        varcolpais: '',
        varpais: '',
        variable1: '',
        variable2: '',
        cantidad:''
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
            let respuesta = await fetch('http://localhost:4000/consulta7', configuracion)
            let json = await respuesta.json();
            console.log('valor de la respuesta json')
            console.log(json)
            imagenmostrar.img = "data:image/png;base64, "+json.img
            imagenmostrar.img2 = "data:image/png;base64, "+json.img2
            imagenmostrar.ecuacion = json.ecuacion

            console.log("valor del mse en react")
            var varcant = json.cantidadmuertes
            
            imagenmostrar.cantidadmuertes = varcant.substring(1, varcant.length-1)
            console.log(imagenmostrar.cantidadmuertes)

            if(imagenmostrar.cantidadmuertes < 100){
                imagenmostrar.conclusion='Se puede apreciar que la cantidad de infectados segun la cantidad de fechas\ningresadas son menores a 100, podemos apreciar que el nivel de contagios\ndentro de este pais, es muy bajo, cuentan con una de las mejores tasas de\ninfeccion a nivel mundial, se insta a seguir manteniendo sus normas de\nbioseguridad.'
            }else if(imagenmostrar.cantidadmuertes > 100 && imagenmostrar.cantidadmuertes < 1000){
                imagenmostrar.conclusion='Se puede apreciar que la cantidad de infectados segun la cantidad de fechas\ningresadas son menores a 1000, podemos apreciar que el nivel de contagios\ndentro de este pais, son elevados, no obstante se recomienda la vacunacion\npara cada habitante en este Pais, aumentar medidas de bioseguridad para\ncontener con mayor fuerza la cantidad de infectados.'
            }else if(imagenmostrar.cantidadmuertes >1000 && imagenmostrar.cantidadmuertes < 10000){
                imagenmostrar.conclusion='Se puede apreciar que la cantidad de infectados segun la cantidad de fechas\ningresadas son menores a 10000 pero mayores a 1000 infectados, podemos\napreciar que el nivel de contagios dentro de este pais, son elevados,\nse recomienda con alta urgencia aplicar nuevas medidas de contencion\npara afrontar este virus y disminuir la cantidad de personas infectadas.'
            }else if(imagenmostrar.cantidadmuertes > 10000){
                imagenmostrar.conclusion='Se puede apreciar que la cantidad de infectados segun la cantidad de fechas\ningresadas son mayores a 10000, podemos apreciar que el nivel de contagios\ndentro de este pais, es alarmante, se recomienda con alta urgencia aplicar\nnuevas medidas de contencion para afrontar este virus y disminuir la cantidad\nde personas infectadas.'
            }
            //console.log(imagenmostrar.pendiente)
        } catch (error) {

        }
    }

    function descargar(){
        var doc = new jsPDF('p', 'pt');
        doc.setFont('Comic Sans','italic')
        doc.text(20, 20, 'Universidad San Calos de Guatemala\nFacultad de Ingenieria\nEscuela de Ciencias y Sistemas\nOLC2')
  
        doc.setFont('Arial', 'normal')
        doc.text('Tendencia del número de infectados por día de un País.',130,130 )
        doc.text(20, 160, 'La covid-19, la enfermedad provocada por el nuevo coronavirus, fue reportada\npor primera vez a fines de 2019 en China. A mediados de enero de 2021\nse pasó la marca de los dos millones de fallecidos a nivel mundial, según el conteo\nde la Universidad Johns Hopkins, y ya se superó los 100 millones de casos confirmados.')      
        doc.text(20, 270, 'Grafica de aplicacion del modelo de regresion polinomial para una tendencia\nde infeccion de COVID-19:')
        doc.addImage(imagenmostrar.img,'PNG',100,310,380,280)
        doc.addImage(fiusac,'PNG',470,10,75,75)
        doc.text(100,620,'Ecuacion polinomial de grado 2:')
        doc.setTextColor(0,0,255)
        doc.text(50,640,imagenmostrar.ecuacion)
        doc.setTextColor(0,0,0)
        doc.text(100,660,'Ultimo registro de muertes en el pais')
        doc.setTextColor(0,0,255)
        doc.text(150,680,imagenmostrar.cantidadmuertes)
        doc.setTextColor(50,50,50)
        doc.setTextColor(0,0,0)
        doc.text(100,700,'Conclusion de analisis de muertes en el Pais:')
        doc.setTextColor(0,0,255)
        doc.text(50,720,imagenmostrar.conclusion)
        doc.setTextColor(50,50,50)
        doc.setFont('Comic Sans','italic')
        doc.setFontSize('13')
        doc.text(355,810,'Autor: Wilfred Stewart Perez Solorzano\nCarnet:201408419')
        doc.addPage()
        doc.setFont('Arial', 'normal')
        doc.text(200,30,'Media de infectados por dia en un pais')
        doc.addImage(imagenmostrar.img2,'PNG',50,40,520,400)
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
                    <Reporte7 contenido={imagenmostrar} />                  
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
                <center><h2>Tendencia del número de infectados por día de un País.</h2></center>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Ingrese la columna de Paises</Form.Label>
                    <Form.Control name="varcolpais" type="text" placeholder="Ingrese la columna de los Paises"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese el nombre del Pais</Form.Label>
                    <Form.Control name="varpais" type="text" placeholder="Ingrese el nombre del pais"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de fechas</Form.Label>
                    <Form.Control name="variable1" type="text" placeholder="Ingrese la columna de fechas"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de infeccion</Form.Label>
                    <Form.Control name="variable2" type="text" placeholder="Ingrese la columna de infeccion" onChange={handleuserchange} />
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

export default Consulta7