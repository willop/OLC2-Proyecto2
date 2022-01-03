import React from 'react'

const Reporte22=({contenido}) => {
    return(
        <div id="ID_reporte" >
                <div id="ID_imagen_reporte">
                    <center><h1>GRAFICA PARA LA TASA DE MORTALIDAD EN UN PAIS</h1></center>                  
                    <center><img src={contenido.img}/></center>
                </div>
                <div id="ID_reporte_contenido">
                    <center>
                    <h2>Tasa de mortalidad por coronavirus (COVID-19) en un país.</h2>
                    <p>
                    El estudio surgió de la avalancha de información relacionada con la COVID, la enfermedad causada por el coronavirus SARS-2, que apuntaba a que la edad se asociaba a mayor mortalidad. Sin embargo, no había evidencia sólida para saber qué debía considerarse “edad avanzada” para esta enfermedad. Al mismo tiempo, se estaban comunicando gran cantidad de casos de fallecimientos en gente joven.
                    </p>
                    <br/>
                    <p>
                    Tasa de mortalidad por coronavirus (COVID-19) en un país.:<br/>
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

export default Reporte22;