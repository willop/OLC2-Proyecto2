import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import "../components/style/Consulta1.css";
import logo from "./IMG/preview.png"
import Reporte20 from "../components/Report/Reporte20"
import {jsPDF} from 'jspdf'


const Consulta20 = (props) => {

    const [switchComp, setSwitch] = useState(false);
    const [imagenmostrar,setimg]=useState({
        img: logo,
        tasa: '20',
        img2: logo,
        tasa2: '40',
        conclusion: '',
        
        
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
            let respuesta = await fetch('http://localhost:4000/consulta20', configuracion)
            let json = await respuesta.json();
            console.log('valor de la respuesta json')
            console.log(json)
            imagenmostrar.img = "data:image/png;base64, "+json.img
            imagenmostrar.tasa = json.tasa
            imagenmostrar.img2 = "data:image/png;base64, "+json.img2
            imagenmostrar.tasa2 = json.tasa2
            
            imagenmostrar.tasa1 < imagenmostrar.tasa2 ? imagenmostrar.conclusion='Se puede evidenciar en la comparacion que la tasa de mortalidad\nes mayor a la tasa de cresimiento de casos confirmados\nen este rango de tiempo especifico': imagenmostrar.conclusion='Se puede evidenciar en la comparacion que la tasa de crecimiento\nde casos confirmados es mayor a la tasa de mortalidad en este rango de\ntiempo especifico'
            //console.log(imagenmostrar.pendiente)
        } catch (error) {

        }
    }

    function descargar(){
        var doc = new jsPDF('p', 'pt');
        doc.setFont('Comic Sans','italic')
        doc.text(20, 20, 'Universidad San Calos de Guatemala\nFacultad de Ingenieria\nEscuela de Ciencias y Sistemas\nOLC2')
  
        doc.setFont('Arial', 'normal')
        doc.text('Tasa de comportamiento de casos activos en relación al número de muertes\n                                                        en un continente.',40,130 )
        doc.text(20, 180, 'El estudio surgió de la avalancha de información relacionada con la COVID,\nla enfermedad causada por el coronavirus SARS-2, que apuntaba a que la edad se asociaba\na mayor mortalidad. Sin embargo, no había evidencia sólida para saber qué debía\nconsiderarse “edad avanzada” para esta enfermedad.\nAl mismo tiempo, se estaban comunicando gran cantidad de casos de fallecimientos en\ngente joven.')      
        doc.text(20, 310, 'Grafica de Tasa de comportamiento de casos activos en relación al número de\nmuertes en un continente de COVID-19:')
        doc.addImage(imagenmostrar.img,'PNG',50,360,500,340)
        doc.text(60,730,'Tasa de comportamiento de casos activos en relación al número de muertes\nen un continente.:')
        doc.setTextColor(255,0,25)
        doc.text(180,780,imagenmostrar.tasa)
        doc.setTextColor(50,50,50)
        doc.setFont('Comic Sans','italic')
        doc.setFontSize('13')
        doc.text(355,810,'Autor: Wilfred Stewart Perez Solorzano\nCarnet:201408419')
        
        doc.addPage()
        doc.setFont('Arial', 'normal')
        doc.setFontSize('18')
        doc.text(20, 50, 'Grafica de Tasa de comportamiento de casos activos en relación al número de\nmuertes en un continente de COVID-19:')
        doc.addImage(imagenmostrar.img2,'PNG',50,90,500,340)
        doc.text(60,450,'Tasa de mortalidad de casos de COVID-19 en relación con nuevos casos\ninfectados:')
        doc.setTextColor(255,0,25)
        doc.text(180,490,imagenmostrar.tasa2)
        doc.setTextColor(0,0,0)
        doc.text(60,510,'Conclusion:')
        doc.setTextColor(0,0,255)
        doc.text(80,530,imagenmostrar.conclusion)
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
                    <Reporte20 contenido={imagenmostrar} />                  
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
                <center><h2>Tasa de crecimiento de casos de COVID-19 en relación con nuevos casos diarios y tasa de muerte por COVID-19.</h2></center>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Ingrese la columna del Pais</Form.Label>
                    <Form.Control name="varcolpais" type="text" placeholder="Ingrese la columna de los Pais"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese el nombre del Pais</Form.Label>
                    <Form.Control name="varpais" type="text" placeholder="Ingrese el nombre del Pais"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de Infectados</Form.Label>
                    <Form.Control name="variable1" type="text" placeholder="Ingrese la columna de infectados"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de muertes</Form.Label>
                    <Form.Control name="variable2" type="text" placeholder="Ingrese la columna de muertes" onChange={handleuserchange} />
                    <Form.Label>Ingrese la columna de infectados diarios</Form.Label>
                    <Form.Control name="variable3" type="text" placeholder="Ingrese la columna de infectados diarios" onChange={handleuserchange} />
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

export default Consulta20