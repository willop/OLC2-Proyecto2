import React from 'react'

const Reporte17=({contenido}) => {
    return(
        <div id="ID_reporte" >
                <div id="ID_imagen_reporte">
                    <center><h1>GRAFICA DE PORCENTAJE DE TASA DE COMPORTAMIENTO</h1></center>                  
                    <center><img src={contenido.img}/></center>
                </div>
                <div id="ID_reporte_contenido">
                    <center>
                    <h2>Tasa de comportamiento de casos activos en relación al número de muertes en un continente.</h2>
                    <p>
                    El estudio surgió de la avalancha de información relacionada con la COVID, la enfermedad causada por el coronavirus SARS-2, que apuntaba a que la edad se asociaba a mayor mortalidad. Sin embargo, no había evidencia sólida para saber qué debía considerarse “edad avanzada” para esta enfermedad. Al mismo tiempo, se estaban comunicando gran cantidad de casos de fallecimientos en gente joven.
                    </p>
                    <br/>
                    <p>
                    Tasa de comportamiento de casos activos en relación al número de muertes en un continente.:<br/>
                       {contenido.tasa}<br/>
                    </p>                        
                    <p>   
                       Autor: Wilfred Stewart Perez Solorzano<br/>Carnet:201408419
                    </p>
                    </center>
                </div>
            </div>
    )
}

export default Reporte17;