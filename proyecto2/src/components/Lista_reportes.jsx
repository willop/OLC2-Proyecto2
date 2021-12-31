import React, { Component } from 'react';
import { Button,Card } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import "./style/Lista_reportes.css";

export class Lista_reportes extends Component {

    render() {

        return (
            <div id="lista_report">
                <Card style={{ width: '20rem' }} id="card-covid">
                    <Card.Img variant="top" src="https://sm.mashable.com/mashable_pk/photo/default/covid_5vu4.jpg" />
                    <Card.Body>
                        <Card.Title>Card Title</Card.Title>
                        <Card.Text>
                        La enfermedad por coronavirus (COVID‑19) es una enfermedad infecciosa provocada por el virus SARS-CoV-2.
                        </Card.Text>
                    </Card.Body>
                </Card>
                
                <div className="d-grid gap-4">
                    <Button variant="light" size="lg">
                        <a href="/consulta1" >Tendencia de la infección por Covid-19 en un País.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/consulta2" >Predicción de Infectados en un País.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/consulta3" >Indice de Progresión de la pandemia.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/consulta4" >Predicción de mortalidad por COVID en un Departamento.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/consulta5" >Predicción de mortalidad por COVID en un País.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/consulta6" >Análisis del número de muertes por coronavirus en un País.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/consulta7" >Tendencia del número de infectados por día de un País.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/consulta8" >Predicción de casos de un país para un año.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/consulta9" >Tendencia de la vacunación de en un País.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/consulta10" >Ánalisis Comparativo de Vacunaciópn entre 2 paises.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/" >Porcentaje de hombres infectados por covid-19 en un País desde el primer caso activo</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/" >Ánalisis Comparativo entres 2 o más paises o continentes.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/" >Muertes promedio por casos confirmados y edad de covid 19 en un País.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/" >Muertes según regiones de un país - Covid 19.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/" >Tendencia de casos confirmados de Coronavirus en un departamento de un País.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/" >Porcentaje de muertes frente al total de casos en un país, región o continente.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/" >Tasa de comportamiento de casos activos en relación al número de muertes en un continente.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/" >Comportamiento y clasificación de personas infectadas por COVID-19 por municipio en un País.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/" >Predicción de muertes en el último día del primer año de infecciones en un país.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/" >Tasa de crecimiento de casos de COVID-19 en relación con nuevos casos diarios y tasa de muerte por COVID-19</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/" >Predicciones de casos y muertes en todo el mundo - Neural Network MLPRegressor</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/" >Tasa de mortalidad por coronavirus (COVID-19) en un país.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/" >Factores de muerte por COVID-19 en un país.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/" >Comparación entre el número de casos detectados y el número de pruebas de un país.</a>
                    </Button>
                    <Button variant="light" size="lg">
                        <a href="/" >Predicción de casos confirmados por día</a>
                    </Button>
                </div>
            </div>

        )
    }
}
