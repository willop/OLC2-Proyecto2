import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import "../components/style/Consulta1.css";
import logo from "./IMG/preview.png"
import Reporte10 from "../components/Report/Reporte10"
import {jsPDF} from 'jspdf'
import fiusac from "./IMG/logo+fiusac.png"

const Consulta10 = (props) => {

    const [switchComp, setSwitch] = useState(false);
    const [imagenmostrar,setimg]=useState({
        img: logo,
        ecuacion: 'y= ax+b',
        mse:'',
        r_cuadrado:'',
        ecuacion2: '',
        mse2:'',
        r_cuadrado2:'',   
        conclusion:'',     
    })
    
    
    const [datos, setDatos] = useState({
        varcolpais: '',
        varpais: '',
        varpais2:'',
        variable1: '',
        variable2: '',
        variable3: '',
        variable4: '',

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
            let respuesta = await fetch('http://34.139.88.235:4000/consulta10', configuracion)
            let json = await respuesta.json();
            console.log('valor de la respuesta json')
            console.log(json)
            imagenmostrar.img = "data:image/png;base64, "+json.img
            
            // esto es para la primera ecuacion
            imagenmostrar.ecuacion = json.ecuacion
            console.log("ecuacion: "+imagenmostrar.ecuacion)
            var variable = json.mse
            imagenmostrar.mse = parseFloat(variable).toFixed(4)
            console.log(imagenmostrar.mse)
            console.log("R al cuadrado")
            variable = json.r_cuadrado
            imagenmostrar.r_cuadrado = parseFloat(variable).toFixed(4)
            
            // esto es para la segunda ecuacion
            imagenmostrar.ecuacion2 = json.ecuacion2
            console.log("ecuacion: "+imagenmostrar.ecuacion2)
            variable = json.mse2
            imagenmostrar.mse2 = parseFloat(variable).toFixed(4)
            console.log(imagenmostrar.mse2)
            console.log("R al cuadrado2")
            variable = json.r_cuadrado2
            imagenmostrar.r_cuadrado2 = parseFloat(variable).toFixed(4)

            imagenmostrar.r_cuadrado < imagenmostrar.r_cuadrado2 ? imagenmostrar.conclusion='Se puede observar que  la vacunacion en el primer pais\ncuenta con uma mejor dispersion de datos que el primer pais':imagenmostrar.conclusion='Se puede observar que  la vacunacion en el segundo pais\ncuenta con uma mejor dispersion de datos que el segundo pais'
                           
            //console.log(imagenmostrar.pendiente)
        } catch (error) {

        }
    }

    function descargar(){
        var doc = new jsPDF('p', 'pt');
        doc.setFont('Comic Sans','italic')
        doc.text(20, 20, 'Universidad San Calos de Guatemala\nFacultad de Ingenieria\nEscuela de Ciencias y Sistemas\nOLC2')
  
        doc.setFont('Arial', 'normal')
        doc.text('Ánalisis Comparativo de Vacunaciópn entre 2 paises.',130,130 )
        doc.text(20, 160, 'Grafica de aplicacion del modelo de regresion polinomial para dos paises')
        doc.addImage(imagenmostrar.img,'PNG',100,180,380,280)
        doc.addImage(fiusac,'PNG',470,10,75,75)
        doc.text(100,470,'Ecuacion polinomial de grado 2 para el primer pais:')
        doc.setTextColor(0,0,255)
        doc.text(130,490,imagenmostrar.ecuacion)
        doc.setTextColor(0,0,0)
        doc.text(100,510,'Error cuadratico medio para primer pais')
        doc.setTextColor(0,0,255)
        doc.text(130,530,imagenmostrar.mse)
        doc.setTextColor(50,50,50)
        doc.setTextColor(0,0,0)
        doc.text(100,550,'Coeficiente de determinacion(R^2):')
        doc.setTextColor(0,0,255)
        doc.text(130,570,imagenmostrar.r_cuadrado)
        doc.setTextColor(0,0,0)
        doc.text(250,600,'Segundo Pais')
        doc.text(100,620,'Ecuacion polinomial de grado 2 para el primer pais:')
        doc.setTextColor(227,66,51)
        doc.text(130,640,imagenmostrar.ecuacion)
        doc.setTextColor(0,0,0)
        doc.text(100,660,'Error cuadratico medio para primer pais')
        doc.setTextColor(227,66,51)
        doc.text(130,680,imagenmostrar.mse)
        doc.setTextColor(50,50,50)
        doc.setTextColor(0,0,0)
        doc.text(100,700,'Coeficiente de determinacion(R^2):')
        doc.setTextColor(227,66,51)
        doc.text(130,720,imagenmostrar.r_cuadrado)
        doc.setTextColor(0,0,0)
        doc.text(100,740,'Conclusion:')
        doc.setTextColor(0,0,0)
        doc.text(130,760,imagenmostrar.conclusion)
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
                    <Reporte10 contenido={imagenmostrar} />                  
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
            <center><h2>Ánalisis Comparativo de Vacunaciópn entre 2 paises..</h2><br/></center>        
            <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Ingrese la columna del Pais</Form.Label>
                    <Form.Control name="varcolpais" type="text" placeholder="Ingrese la columna del primer Pais"  onChange={handleuserchange}/>
                </Form.Group>
                <center><h2>Primer Pais</h2></center>
                
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Ingrese el nombre del primer Pais</Form.Label>
                    <Form.Control name="varpais" type="text" placeholder="Ingrese el nombre del primer Pais"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de fechas para el primer pais</Form.Label>
                    <Form.Control name="variable1" type="text" placeholder="Ingrese la columna de fechas para el primer Pais"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de vacunacion del primer pais</Form.Label>
                    <Form.Control name="variable2" type="text" placeholder="Ingrese la columna de vacunacion para el primer pais" onChange={handleuserchange} />
                </Form.Group>
                <br/>
                <center><h2>Segundo Pais</h2></center>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Ingrese el nombre del segundo Pais</Form.Label>
                    <Form.Control name="varpais2" type="text" placeholder="Ingrese el nombre del segundo Pais"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de fechas para el segundo pais</Form.Label>
                    <Form.Control name="variable3" type="text" placeholder="Ingrese la columna de fechas para el segundo Pais"  onChange={handleuserchange}/>
                    <Form.Label>Ingrese la columna de vacunacion del segundo pais</Form.Label>
                    <Form.Control name="variable4" type="text" placeholder="Ingrese la columna de vacunacion para el segundo pais" onChange={handleuserchange} />
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

export default Consulta10