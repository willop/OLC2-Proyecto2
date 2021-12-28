import React, { Component } from 'react'
import { FormGroup, Input } from 'reactstrap';
import { Form,Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import "../components/style/Consulta1.css"


export class Consulta1 extends Component {

    constructor(props) {
        super(props);
        this.state ={
            variable1: '', 
            variable2: '',
            file: '',
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


    enviarDatos(){
        console.log(this.state);
    }

    render() {
        return (
            <div id="ID_consulta">
                <FormGroup>
                    <Input id="exampleFile" name="file" type="file" value={this.state.file} onChange={this.handleInputChange}/>
                </FormGroup>

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