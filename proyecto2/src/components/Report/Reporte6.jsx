import React from 'react'

const Reporte1=({contenido}) => {
    return(
        <div id="ID_reporte" >
                <div id="ID_imagen_reporte">
                    <center><h1>GRAFICA DEL ANALISIS</h1></center>
                    
                    <center><img src={contenido.img}/></center>
                </div>
                <div id="ID_reporte_contenido">
                    <center>
                    <h2>Análisis del número de muertes por coronavirus en un País.</h2>
                    <p>
                    La covid-19, la enfermedad provocada por el nuevo coronavirus, fue reportada por primera vez a fines de 2019 en China.<br/>A mediados de enero de 2021 se pasó la marca de los dos millones de fallecidos a nivel mundial, según el conteo de la Universidad Johns Hopkins, y ya se superó los 100 millones de casos confirmados.
                    </p>
                    <br/>
                    <p>
                       Ecuacion polinomial de grado 2:<br/>
                       {contenido.ecuacion}<br/>
                       Cantidad de muertes en este Pais:<br/>
                       {contenido.cantidadmuertes}<br/>
                       conclusion:<br/>
                       {contenido.conclusion}<br/>
                       <br/>
                       <br/>
                       Autor: Wilfred Stewart Perez Solorzano<br/>Carnet:201408419
                    </p>
                    </center>
                </div>
            </div>
    )
}

export default Reporte1;