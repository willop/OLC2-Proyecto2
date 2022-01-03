import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap';
import {ButtonGroup} from 'reactstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import "../components/style/Consulta1.css";
import logo from "./IMG/preview.png"
import Reporte19 from "../components/Report/Reporte19"
import { jsPDF } from 'jspdf'
import fiusac from "./IMG/logo+fiusac.png"



const Consulta19 = (props) => {

    const [switchComp, setSwitch] = useState(false);
    const [imagenmostrar, setimg] = useState({
        img: logo,
        mse: 'y= ax+b',
        val_r_cuadrado: '',
        aprox: ''

    })


    const [datos, setDatos] = useState({
        varcolpais: '',
        varpais: '',
        variable1: '',
        variable2: '',
    })
    const handleuserchange = (event) => {
        setDatos({ ...datos, [event.target.name]: event.target.value })
    }


    const enviarDatos = async (event) => {
        console.log("datos:" + datos.varcolpais + "\nContrasenia:" + datos.varpais)
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
            let respuesta = await fetch('http://localhost:4000/consulta19', configuracion)
            let json = await respuesta.json();
            console.log('valor de la respuesta json')
            console.log(json)
            imagenmostrar.img = "data:image/png;base64, " + json.img
            imagenmostrar.ecuacion = json.ecuacion

            console.log("valor del mse en react")
            imagenmostrar.mse = 'y = ' + json.mse
            console.log(imagenmostrar.mse)

            console.log("valor del coeficiente en react")
            imagenmostrar.val_r_cuadrado = parseFloat(json.val_r_cuadrado).toFixed(3)
            console.log(imagenmostrar.val_r_cuadrado)

            imagenmostrar.aprox = json.aprox
            //console.log(imagenmostrar.pendiente)
        } catch (error) {

        }
    }

    function descargar() {
        var doc = new jsPDF('p', 'pt');
        doc.setFont('Comic Sans', 'italic')
        doc.text(20, 20, 'Universidad San Calos de Guatemala\nFacultad de Ingenieria\nEscuela de Ciencias y Sistemas\nOLC2')

        doc.setFont('Arial', 'normal')
        doc.text('Predicción de casos de un país para un año.', 150, 130)
        doc.text(20, 160, 'A partir de los datos registrados, hemos podido desarrollar un modelo matemático\nque refleja el flujo de la población entre los diferentes grupos de interés en relación\ncon la COVID-19. Esta herramienta permite analizar diferentes escenarios basados\nn medidas de restricción socio-sanitarias y pronosticar el número de infectados,\nhospitalizados e ingresados en UCI.')
        doc.text(20, 280, 'Manual de aplicacion del modelo de regresion polinomial para una prediccion\nde la infeccion de COVID-19 a un año:')
        doc.addImage(imagenmostrar.img, 'PNG', 100, 320, 400, 280)
        doc.addImage(fiusac,'PNG',470,10,75,75)
        doc.text(100, 620, 'Ecuacion polinomial de grado 2:')
        doc.setTextColor(0, 0, 255)
        doc.text(150, 640, imagenmostrar.mse)
        doc.setTextColor(0, 0, 0)
        doc.text(100, 660, 'Coeficiente determinacion(R^2)')
        doc.setTextColor(0, 0, 255)
        doc.text(150, 680, imagenmostrar.val_r_cuadrado)
        doc.setTextColor(50, 50, 50)
        doc.setTextColor(0, 0, 0)
        doc.text(100, 700, 'Cantidad de muertes aproximadas utilizando la ecuacion son:')
        doc.setTextColor(0, 0, 255)
        doc.text(150, 720, imagenmostrar.aprox)
        doc.setTextColor(50, 50, 50)
        doc.setFont('Comic Sans', 'italic')
        doc.setFontSize('13')
        doc.text(355, 810, 'Autor: Wilfred Stewart Perez Solorzano\nCarnet:201408419')
        doc.save('demo.pdf')
    }

    function Componente() {
        if (switchComp) {
            return (
                <div>
                    <Reporte19 contenido={imagenmostrar} />
                </div>
            )
        } else {
            return (
                <div >
                    <br />
                    <br />
                    <br /><center>
                        <h1 id="id_prev_reporte">Reporte</h1>
                    </center>
                </div>
            )
        }
    }

    function verpreview() {
        setSwitch(!switchComp)
    }


    return (
        <div id="ID_general">
            <div id="ID_consulta">
                <center><h2>Predicción de muertes en el último día del primer año de infecciones en un país..</h2></center>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Ingrese la columna del Pais</Form.Label>
                    <Form.Control name="varcolpais" type="text" placeholder="Ingrese la columna del Pais" onChange={handleuserchange} />
                    <Form.Label>Ingrese el nombre del Pais</Form.Label>
                    <Form.Control name="varpais" type="text" placeholder="Ingrese el nombre del Pais" onChange={handleuserchange} />
                    <Form.Label>Ingrese la columna de Fechas</Form.Label>
                    <Form.Control name="variable1" type="text" placeholder="Ingrese la columna de fechas" onChange={handleuserchange} />
                    <Form.Label>Ingrese la columna de Mortalidad</Form.Label>
                    <Form.Control name="variable2" type="text" placeholder="Ingrese la columna de Mortalidad" onChange={handleuserchange} />
                </Form.Group>
                
                <Button variant="danger" id="boton_enviar" onClick={enviarDatos}>Enviar</Button>
            </div>
            <br />
            <Button variant="info" id="boton_enviar" onClick={verpreview}>* Preview *</Button>
            <Componente />

            <div id="ID_div_boton">
                <Button variant="success" id="descargar" onClick={descargar} >Descargar reporte</Button>
            </div>

        </div>//div global
    )

}

export default Consulta19