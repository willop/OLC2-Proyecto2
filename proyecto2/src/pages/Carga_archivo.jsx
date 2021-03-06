import React, { Component } from 'react';
import { FormGroup, Input } from 'reactstrap';
import { Form,Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../components/style/CargaArchivo.css'


export class Carga_archivo extends Component {


    enviarDatos(e){
        window.location = "/";
    }

    changeText= async e => {
        try {
            let formdata = new FormData();
            formdata.append('files',e.target.files[0]);
            console.log(formdata);
             
            let configuracion = {
                method: 'POST',
                headers: {
                },
                body: formdata
            }
            let respuesta = await fetch('http://34.139.88.235:4000/cargamasiva',configuracion)
            let json = await respuesta.json();
            console.log(json)
            
        } catch (error) {
            
        }
        console.log("Redireccionamiento")

    }
    render() {
        return (
            <div>
                    <br/>
                    <br/>
                    <br/>
                <div id='ID_letrero'>
                    <center><h1>Cargar archivo (.csv,xlxs o xls)</h1></center>
                </div>
                <br/>
                <br/>
                <FormGroup>
                    <Input id="exampleFile" name="files" type="file" accept=".json, .csv, .xls, .xlsx" onChange={this.changeText}/>
                    <Button variant="outline-info" id="boton_enviar" onClick={() => this.enviarDatos()}>Listo</Button>
                </FormGroup>                
            </div>
        )
    }
}
