import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import "../components/style/Consulta1.css";
import logo from "./IMG/preview.png"
import Reporte18 from "../components/Report/Reporte18"
import {jsPDF} from 'jspdf'
import fiusac from "./IMG/logo+fiusac.png"

const Consulta18 = (props) => {

    const [switchComp, setSwitch] = useState(false);
    const [imagenmostrar,setimg]=useState({
        img: logo,
        ecuacion: 'y= ax+b',
        mse:'',
        r_cuadrado:'',
        conclusion:'',
        
    })
    
    
    const [datos, setDatos] = useState({
        varcolpais: '',
        varpais: '',
        varcolmuni: '',
        varmuni: '',
        variable1: '',
        variable2: '',
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
            let respuesta = await fetch('http://34.139.88.235:4000/consulta18', configuracion)
            let json = await respuesta.json();
            console.log('valor de la respuesta json')
            console.log(json)
            imagenmostrar.img = "data:image/png;base64, "+json.img
            imagenmostrar.conclusion = 'En esta graficae observa el comportamiento del municipio de\n'+imagenmostrar.varmuni +' segun la cantidad de personas infectadas en el transcurso\nde un determinado tiempo.'
                     
            
            //console.log(imagenmostrar.pendiente)
        } catch (error) {

        }
    }

    function descargar(){
        var doc = new jsPDF('p', 'pt');
        doc.setFont('Comic Sans','italic')
        doc.text(20, 20, 'Universidad San Calos de Guatemala\nFacultad de Ingenieria\nEscuela de Ciencias y Sistemas\nOLC2')
  
        doc.setFont('Arial', 'normal')
        doc.setFontSize('13')
        doc.text(' Comportamiento y clasificaci??n de personas infectadas por COVID-19 por municipio en un Pa??s.',60,130 )
        doc.setFontSize('17')
        doc.text(20, 160, 'La covid-19, la enfermedad provocada por el nuevo coronavirus, fue reportada\npor primera vez a fines de 2019 en China. A mediados de enero de 2021\nse pas?? la marca de los dos millones de fallecidos a nivel mundial, seg??n el conteo\nde la Universidad Johns Hopkins, y ya se super?? los 100 millones de casos confirmados.')      
        doc.text(20, 270, 'Grafica de aplicacion del modelo comporamiento de las personas de un municipio\nde COVID-19:')
        doc.addImage(imagenmostrar.img,'PNG',100,310,380,280)
        doc.addImage(fiusac,'PNG',470,10,75,75)
        doc.text(100,620,'Conclusion:')
        doc.setTextColor(0,0,255)
        doc.text(50,640,imagenmostrar.conclusion)
        doc.setTextColor(0,0,0)
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
                    <Reporte18 contenido={imagenmostrar} />                  
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
                <center><h2>Comportamiento y clasificaci??n de personas infectadas por COVID-19 por municipio en un Pa??s.</h2></center>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Ingrese la columna de Paises</Form.Label>
                    <Form.Control name="varcolpais" type="text" placeholder="Ingrese la columna de los Paises"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese el nombre del Pais</Form.Label>
                    <Form.Control name="varpais" type="text" placeholder="Ingrese la columna del Pais"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de los Municipios</Form.Label>
                    <Form.Control name="varcolmuni" type="text" placeholder="Ingrese el nombre la columna municipio"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese el nombre del Municipio</Form.Label>
                    <Form.Control name="varmuni" type="text" placeholder="Ingrese el nombre del municipio"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de fechas</Form.Label>
                    <Form.Control name="variable1" type="text" placeholder="Ingrese la columna de fechas"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de infectados</Form.Label>
                    <Form.Control name="variable2" type="text" placeholder="Ingrese la columna de infectados" onChange={handleuserchange} />
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

export default Consulta18