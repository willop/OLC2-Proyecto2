import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import "../components/style/Consulta1.css";
import logo from "./IMG/preview.png"
import Reporte17 from "../components/Report/Reporte17"
import {jsPDF} from 'jspdf'
import fiusac from "./IMG/logo+fiusac.png"


const Consulta17 = (props) => {

    const [switchComp, setSwitch] = useState(false);
    const [imagenmostrar,setimg]=useState({
        img: logo,
        tasa: '20',
        conclusion:'',
    })
    
    
    const [datos, setDatos] = useState({
        varcolpais: '',
        varpais: '',
        variable1: '',
        variable2: '',
        variable3: ''
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
            let respuesta = await fetch('http://localhost:4000/consulta17', configuracion)
            let json = await respuesta.json();
            console.log('valor de la respuesta json')
            console.log(json)
            imagenmostrar.img = "data:image/png;base64, "+json.img
            imagenmostrar.tasa = json.tasa

            imagenmostrar.tasa < 1 ? imagenmostrar.conclusion = 'Ya que la tasa de casos activos esta por debajo de 0.5 se concluye que\nla cantidad de personas muertas es menor que el de las personas infectadas.' : imagenmostrar.conclusion = 'Ya que la tasa de casos activos esta por encima de 0.5 se concluye\nque la cantidad de personas infectadas es menor que el de las personas muertas'
            
            //console.log(imagenmostrar.pendiente)
        } catch (error) {

        }
    }

    function descargar(){
        var doc = new jsPDF('p', 'pt');
        doc.setFont('Comic Sans','italic')
        doc.text(20, 20, 'Universidad San Calos de Guatemala\nFacultad de Ingenieria\nEscuela de Ciencias y Sistemas\nOLC2')
  
        doc.setFont('Arial', 'normal')
        doc.setFontSize('14')
        doc.text('Tasa de comportamiento de casos activos en relación al número de muertes en un continente.',40,130 )
        doc.text(20, 160, 'El estudio surgió de la avalancha de información relacionada con la COVID,\nla enfermedad causada por el coronavirus SARS-2, que apuntaba a que la edad se asociaba\na mayor mortalidad. Sin embargo, no había evidencia sólida para saber qué debía\nconsiderarse “edad avanzada” para esta enfermedad.\nAl mismo tiempo, se estaban comunicando gran cantidad de casos de fallecimientos en\ngente joven.')      
        doc.text(20, 270, 'Grafica de Tasa de comportamiento de casos activos en relación al número de\nmuertes en un continente de COVID-19:')
        doc.addImage(imagenmostrar.img,'PNG',50,310,450,300)
        doc.addImage(fiusac,'PNG',470,10,75,75)
        doc.text(60,650,'Tasa de comportamiento de casos activos en relación al número de muertes\nen un continente.:')
        doc.setTextColor(255,0,25)
        doc.text(100,690,imagenmostrar.tasa)
        doc.setTextColor(0,0,0)
        doc.text(60,710,'Conclusion:')
        doc.setTextColor(0,0,255)
        doc.text(100,730,imagenmostrar.conclusion)
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
                    <Reporte17 contenido={imagenmostrar} />                  
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
                <center><h2>Tasa de comportamiento de casos activos en relación al número de muertes en un continente.</h2></center>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Ingrese la columna de Continentes</Form.Label>
                    <Form.Control name="varcolpais" type="text" placeholder="Ingrese la columna de los Continentes"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese el nombre del Continente</Form.Label>
                    <Form.Control name="varpais" type="text" placeholder="Ingrese el nombre del Continente"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de fechas</Form.Label>
                    <Form.Control name="variable1" type="text" placeholder="Ingrese la columna de fechas"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de muertes</Form.Label>
                    <Form.Control name="variable2" type="text" placeholder="Ingrese la columna de muertes" onChange={handleuserchange} />
                    <Form.Label>Ingrese la columna de casos activos</Form.Label>
                    <Form.Control name="variable3" type="text" placeholder="Ingrese la columna de casos activos" onChange={handleuserchange} />
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

export default Consulta17