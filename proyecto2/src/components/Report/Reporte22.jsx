import React from 'react'

const Reporte11=({contenido}) => {
    return(
        <div id="ID_reporte" >
                <div id="ID_imagen_reporte">
                    <center><h1>GRAFICA DE PORCENTAJE DE HOMBRES</h1></center>                  
                    <center><img src={contenido.img}/></center>
                </div>
                <div id="ID_reporte_contenido">
                    <center>
                    <h2>Porcentaje de hombres infectados por covid-19 en un País desde el primer caso activo</h2>
                    <p>
                    Las vacunas para prevenir la enfermedad por coronavirus 2019 (COVID-19) tal vez sean la mejor esperanza para terminar con la pandemia. Sin embargo, mientras la Administración de Alimentos y Medicamentos (FDA, por sus siglas en inglés) siga aprobando o autorizando el uso de emergencia de las vacunas contra la COVID-19, es probable que sigas teniendo preguntas.
                    </p>
                    <br/>
                    <p>
                       Cantidad de personas totales infectados:<br/>
                       {contenido.total}<br/>
                       Cantidad de hombres infectados:<br/>
                       {contenido.hombres}<br/>
                       Porcentaje de hombres infectados:<br/>
                       {contenido.porcentaje}<br/>
                    </p>                        
                    <p>   
                       Autor: Wilfred Stewart Perez Solorzano<br/>Carnet:201408419
                    </p>
                    </center>
                </div>
            </div>
    )
}

export default Reporte11;