import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import "../components/style/Consulta1.css";
import logo from "./IMG/preview.png"
import Reporte13 from "../components/Report/Reporte13"
import {jsPDF} from 'jspdf'


const Consulta13 = (props) => {

    const [switchComp, setSwitch] = useState(false);
    const [imagenmostrar,setimg]=useState({
        img: logo,
        img2: 'y= ax+b',
        promedio:'',        
    })
    
     
    const [datos, setDatos] = useState({
        varcolpais: '',
        varpais: '',
        variable1: '',
        variable2: '',
        variable3:''
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
            let respuesta = await fetch('http://localhost:4000/consulta13', configuracion)
            let json = await respuesta.json();
            console.log('valor de la respuesta json')
            console.log(json)
            imagenmostrar.img = "data:image/png;base64, "+json.img
            imagenmostrar.img2 = "data:image/png;base64, "+json.img2

            console.log("mse")
            imagenmostrar.promedio = json.promedio
                                  
            
            //console.log(imagenmostrar.pendiente)
        } catch (error) {

        }
    }

    function descargar(){
        var doc = new jsPDF('p', 'pt');
        doc.setFont('Comic Sans','italic')
        doc.text(20, 20, 'Universidad San Calos de Guatemala\nFacultad de Ingenieria\nEscuela de Ciencias y Sistemas\nOLC2')
  
        doc.setFont('Arial', 'normal')
        doc.text('Muertes promedio por casos confirmados y edad de covid 19 en un País.',100,130 )
        doc.text(20, 160, 'La covid-19, la enfermedad provocada por el nuevo coronavirus, fue reportada\npor primera vez a fines de 2019 en China. A mediados de enero de 2021\nse pasó la marca de los dos millones de fallecidos a nivel mundial, según el conteo\nde la Universidad Johns Hopkins, y ya se superó los 100 millones de casos confirmados.')      
        doc.text(200, 270, 'Grafica de muertes vs infectados')
        doc.addImage(imagenmostrar.img,'PNG',80,290,450,330)
        doc.setTextColor(50,50,50)
        doc.setFont('Comic Sans','italic')
        doc.setFontSize('13')
        doc.text(355,810,'Autor: Wilfred Stewart Perez Solorzano\nCarnet:201408419')
        doc.addPage();
        doc.setFontSize('18')
        doc.setFont('Arial', 'normal')
        doc.text(200,40,'Grafica de muertes vs edad:')
        doc.addImage(imagenmostrar.img2,'PNG',80,60,450,330)
        doc.setTextColor(0,0,0)
        doc.text(250,420,'Muertes promedio')
        doc.setTextColor(255,0,10)
        doc.text(245,440,imagenmostrar.promedio)
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
                    <Reporte13 contenido={imagenmostrar} />                  
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
                <center><h2>Muertes promedio por casos confirmados y edad de covid 19 en un País.</h2></center>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Ingrese la columna de Paises</Form.Label>
                    <Form.Control name="varcolpais" type="text" placeholder="Ingrese la columna de los Paises"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese el nombre del Pais</Form.Label>
                    <Form.Control name="varpais" type="text" placeholder="Ingrese el nombre del pais"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la la columna de muertes</Form.Label>
                    <Form.Control name="variable1" type="text" placeholder="Ingrese la columna de muertes"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna casos confirmados</Form.Label>
                    <Form.Control name="variable2" type="text" placeholder="Ingrese la columna de casos confirmados" onChange={handleuserchange} />
                    <Form.Label>Ingrese la columna edad</Form.Label>
                    <Form.Control name="variable3" type="text" placeholder="Ingrese la columna de edad" onChange={handleuserchange} />
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

export default Consulta13;