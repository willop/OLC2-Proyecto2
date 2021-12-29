import React, { Component } from 'react'
import { Form,Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import "../components/style/Consulta1.css"


export class Consulta1 extends Component {

    constructor(props) {
        super(props);
        this.state ={
            variable1: '', 
            variable2: '',
        }
        this.handleInputChange = this.handleInputChange.bind(this);
    }

    handleInputChange(event) {
        let name=event.target.name;
        let value=event.target.value;
        this.setState({
            [name]: value,
        });
        console.log(this.state);
    }


    enviarDatos= async e => {
        console.log(this.state);
        try {
            let configuracion = {
                method: 'POST',
                headers: {
                    'Accept':'application/json',
                    'Content-Type':'application/json'
                },
                body: JSON.stringify(this.state)
            }
            let respuesta = await fetch('http://localhost:4000/consulta1',configuracion)
            let json = await respuesta.json();
            console.log(json)
        } catch (error) {
            
        }
    }

    render() {
        return (
            <div id="ID_consulta">
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Variable 1</Form.Label>
                    <Form.Control name="variable1" type="text" placeholder="Ingrese la primera variable" value={this.state.variable1} onChange={this.handleInputChange} />
                    <Form.Label>Variable 2</Form.Label>
                    <Form.Control name="variable2" type="text" placeholder="Ingrese la segunda variable" value={this.state.variable2} onChange={this.handleInputChange}/>
                </Form.Group>
                <Button variant="outline-info" id="boton_enviar" onClick={() => this.enviarDatos()}>Enviar</Button>
            </div>
        )
    }
}