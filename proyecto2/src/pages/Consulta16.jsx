import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import "../components/style/Consulta1.css";
import logo from "./IMG/preview.png"
import Reporte16 from "../components/Report/Reporte16"
import {jsPDF} from 'jspdf'
import fiusac from "./IMG/logo+fiusac.png"


const Consulta16 = (props) => {

    const [switchComp, setSwitch] = useState(false);
    const [imagenmostrar,setimg]=useState({
        img: logo,
        porcentaje: '100%',
        total:'1000',
        hombres:'235',
        conclusion:''
        
    })
    
    
    const [datos, setDatos] = useState({
        varcolpais: '',
        varpais: '',
        variable1: '',
        variable2: '',
        vargenero:'',
        namegenero:'',
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
            let respuesta = await fetch('http://34.139.88.235:4000/consulta16', configuracion)
            let json = await respuesta.json();
            console.log('valor de la respuesta json')
            console.log(json)
            imagenmostrar.img = "data:image/png;base64, "+json.img

            imagenmostrar.porcentaje = json.porcentaje

            imagenmostrar.total = json.total
            console.log(imagenmostrar.mse)

            imagenmostrar.hombres = json.hombres
            imagenmostrar.hombres > 50 ?  imagenmostrar.conclusion = 'Se puede evidenciar que la cantidad de hombres infectados no supera\nla mitad de la poblacion infectada, por tanto se recomienda encocarse\nmas en la poblacion de mujeres y brindarme una mayor seguridad frente\nal virus.': imagenmostrar.conclusion = 'Se puede evidenciar que la cantidad de mujeres infectados no supera\nla mitad de la poblacion infectada, por tanto se recomienda encocarse\nmas en la demas poblacion y brindarme una mayor seguridad frente al\nvirus.'
            
            //console.log(imagenmostrar.pendiente)
        } catch (error) {

        }
    }

    function descargar(){
        var doc = new jsPDF('p', 'pt');
        doc.setFont('Comic Sans','italic')
        doc.text(20, 20, 'Universidad San Calos de Guatemala\nFacultad de Ingenieria\nEscuela de Ciencias y Sistemas\nOLC2')
  
        doc.setFont('Arial', 'normal')
        doc.text('Porcentaje de mujeres infectados por covid-19 en un Pa??s, Region o continente',60,130 )
        doc.text(20, 160, 'La covid-19, la enfermedad provocada por el nuevo coronavirus, fue reportada\npor primera vez a fines de 2019 en China. A mediados de enero de 2021\nse pas?? la marca de los dos millones de fallecidos a nivel mundial, seg??n el conteo\nde la Universidad Johns Hopkins, y ya se super?? los 100 millones de casos confirmados.')      
        doc.text(20, 270, 'Grafica de la cantidad de Hombres infectados  vs la poblacion en general:')
        doc.addImage(imagenmostrar.img,'PNG',100,310,380,280)
        doc.addImage(fiusac,'PNG',470,10,75,75)
        doc.text(100,620,'Poblacion total:')
        doc.setTextColor(0,0,255)
        doc.text(200,640,imagenmostrar.total)
        doc.setTextColor(0,0,0)
        doc.text(100,660,'Poblacion de mujeres')
        doc.setTextColor(0,0,255)
        doc.text(200,680,imagenmostrar.hombres)
        doc.setTextColor(50,50,50)
        doc.setTextColor(0,0,0)
        doc.text(100,700,'Porcentaje de mujeres:')
        doc.setTextColor(0,0,255)
        doc.text(200,720,imagenmostrar.porcentaje)
        doc.setTextColor(0,0,0)
        doc.text(100,740,'Conclusion')
        doc.setTextColor(0,0,0)
        doc.sestFontSize('11')
        doc.text(100,760,imagenmostrar.conclusion)
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
                    <Reporte16 contenido={imagenmostrar} />                  
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
                <center><h2>Porcentaje de muertes frente al total de casos en un pa??s, regi??n o continente. </h2></center>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Ingrese la columna de Paises</Form.Label>
                    <Form.Control name="varcolpais" type="text" placeholder="Ingrese la columna de los Paises"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese el nombre del Pais</Form.Label>
                    <Form.Control name="varpais" type="text" placeholder="Ingrese el nombre del pais"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de genero</Form.Label>
                    <Form.Control name="vargenero" type="text" placeholder="Ingrese la columna de genero"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese el valor exacto para "Mujeres"</Form.Label>
                    <Form.Control name="namegenero" type="text" placeholder="Por defecto se bucara por la palabra (Mujer)" onChange={handleuserchange}/>
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

export default Consulta16