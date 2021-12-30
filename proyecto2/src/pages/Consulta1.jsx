import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import "../components/style/Consulta1.css";
import logo from "./IMG/preview.png"
import Reporte from "../components/Reporte"


const Consulta1 = (props) => {

    const [switchComp, setSwitch] = useState(0);
    const [imagenmostrar,setimg]=useState({
        img: logo,
        ecuacion: '',
        val_r_cuadrado:'',
        aproximaciones: '',
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
        //console.log(JSON.stringify(envios))
        //var url ='http://localhost:4000/consulta1'
        try {
            let configuracion = {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            }
            let respuesta = await fetch('http://localhost:4000/consulta1', configuracion)
            let json = await respuesta.json();
            //console.log(json.img)
            setimg({...imagenmostrar,img : "data:image/png;base64, "+json.img})
            console.log("valor de la imagen en react")
            console.log(imagenmostrar.img)
            /*console.log(this.state2.imagenreporte)
            this.state2.estado = json.ecuacion
            console.log(this.state2.estado)
            console.log(json.val_r)
            console.log(json.aproximaciones)
            //console.log(json)*/
        } catch (error) {

        }
    }

    function Componente(){
        //if (switchComp===1) {
            return (
                <div>
                    <Reporte contenido={imagenmostrar} />
                </div>
                
            )
       // }else{
        //    return(
        //        <h1>Reporte</h1>
        //    )
        //}
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
            <div id="ID_div_boton">
                <Button variant="success" id="descargar" >Descargar reporte</Button>
            </div>
        </div>//div global
    )

}

export default Consulta1