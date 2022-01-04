import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import "../components/style/Consulta1.css";
import logo from "./IMG/preview.png"
import Reporte3 from "../components/Report/Reporte3"
import {jsPDF} from 'jspdf'
import fiusac from "./IMG/logo+fiusac.png"


const Consulta3 = (props) => {

    const [switchComp, setSwitch] = useState(false);
    const [imagenmostrar,setimg]=useState({
        img: logo,
        ecuacion: 'y= ax+b',
        indice:'',
        conclusion:''
    })
    
    const [datos, setDatos] = useState({
        varcolpais: '',
        varpais: '',
        variable1: '',
        variable2: ''
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
            let respuesta = await fetch('http://34.139.88.235:4000/consulta3', configuracion)
            let json = await respuesta.json();
            console.log('valor de la respuesta json')
            console.log(json)
            imagenmostrar.img = "data:image/png;base64, "+json.img
            imagenmostrar.ecuacion = json.ecuacion

            console.log("valor del indice en react")
            imagenmostrar.mse = parseFloat( json.indice)
            console.log(imagenmostrar.indice)
            

            imagenmostrar.indice > 1 ?  imagenmostrar.conclusion='La pendiente y la intersección definen la relación lineal entre dos\nvariables, y se pueden utilizar para estimar una tasa de cambio\npromedio. En este modelo en especifico siendo una pendiente mayor a\n1 se, puede concluir que nos referimos a una alta progresion en\nlos datos tendiendo a crecer rapidamente.' : imagenmostrar.conclusion='La pendiente y la intersección definen la relación lineal entre dos\nvariables, y se pueden utilizar para estimar una tasa de cambio\npromedio. En este modelo en especifico siendo una pendiente menor a\n1 se puede concluir que nos baja progresion en los datos tendiendo\na crecer lentamente en el transcurso del tiempo.'
            //console.log(imagenmostrar.pendiente)
        } catch (error) {

        }
    }

    function descargar(){
        var doc = new jsPDF('p', 'pt');
        doc.setFont('Comic Sans','italic')
        doc.text(20, 20, 'Universidad San Calos de Guatemala\nFacultad de Ingenieria\nEscuela de Ciencias y Sistemas\nOLC2')
  
        doc.setFont('Arial', 'normal')
        doc.text('Indice de Progresión de la pandemia.',175,130 )
        doc.text(20, 160, 'A partir de los datos registrados, hemos podido desarrollar un modelo matemático\nque refleja el flujo de la población entre los diferentes grupos de interés en relación\ncon la COVID-19. Esta herramienta permite analizar diferentes escenarios basados\nn medidas de restricción socio-sanitarias y pronosticar el número de infectados,\nhospitalizados e ingresados en UCI.')      
        doc.text(20, 300, 'Manual de aplicacion del modelo de regresion lineal para una tendencia de\ninfeccion de COVID-19:')
        doc.addImage(imagenmostrar.img,'PNG',100,320,380,280)
        doc.addImage(fiusac,'PNG',470,10,75,75)
        doc.text(100,620,'La ecuacion de progresion lineal para este modelo es:')
        doc.setTextColor(0,0,255)
        doc.text(150,640,imagenmostrar.ecuacion)
        doc.setTextColor(0,0,0)
        doc.text(100,660,'Coeficiente progresion es:')
        doc.setTextColor(0,0,255)
        doc.text(150,680,imagenmostrar.mse.toFixed(5))
        doc.setTextColor(50,50,50)
        doc.setTextColor(0,0,0)
        doc.text(100,700,'Conclusion en base al indice de progresion:')
        doc.setTextColor(0,0,255)
        doc.text(80,720,imagenmostrar.conclusion)
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
                    <Reporte3 contenido={imagenmostrar} />                  
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
                <center><h2>Indice de Progresión de la pandemia.</h2></center>
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

export default Consulta3