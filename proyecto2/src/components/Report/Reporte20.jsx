import React from 'react'

const Reporte20 = ({ contenido }) => {
    return (
        <div id="ID_reporte" >
            <div id="ID_imagen_reporte">
                <center><h1>GRAFICA DE PORCENTAJE DE TASA DE COMPORTAMIENTO</h1></center>
                <center><img src={contenido.img} /></center>
            </div>
            <div id="ID_reporte_contenido">
                <center>
                    <h2>Tasa de crecimiento de casos de COVID-19 en relación con nuevos casos diarios</h2>
                    <p>
                        <br />
                        Tasa de comportamiento de casos activos en relación al número de muertes en un continente.:<br />
                        {contenido.tasa}<br />
                    </p>

                    <div id="ID_imagen_reporte">
                        <center><h1>GRAFICA DE PORCENTAJE DE TASA DE COMPORTAMIENTO</h1></center>
                        <center><img src={contenido.img2} /></center>
                    </div>
                    <div id="ID_reporte_contenido">
                        <center>
                            <h2>Tasa de mortalidad de casos de COVID-19 en relación con nuevos casos infectados</h2>
                            <p>
                                <br />
                                Tasa de comportamiento de casos activos en relación al número de muertes en un continente.:<br />
                                {contenido.tasa2}<br />
                                <br/><br/>El estudio surgió de la avalancha de información relacionada con la COVID, la enfermedad causada por el coronavirus SARS-2, que apuntaba a que la edad se asociaba a mayor mortalidad. Sin embargo, no había evidencia sólida para saber qué debía considerarse “edad avanzada” para esta enfermedad. Al mismo tiempo, se estaban comunicando gran cantidad de casos de fallecimientos en gente joven.<br/><br/>
                            </p>
                        </center>
                    </div>
                    <p>
                        Autor: Wilfred Stewart Perez Solorzano<br />Carnet:201408419
                    </p>
                </center>
            </div>
        </div>
    )
}

export default Reporte20;