import React from 'react'

const Reporte13=({contenido}) => {
    return(
        <div id="ID_reporte" >
                <div id="ID_imagen_reporte">
                    <center><h1>Grafica de Muertes promedio por casos confirmados y edad de covid 19 en un País</h1></center>                  
                    <br/>
                    <h2>Muertes vs Casos confirmados</h2>
                    <center><img src={contenido.img}/></center>
                    <br/>
                    <h2>Muertes vs edad</h2>
                    <center><img src={contenido.img2}/></center>
                </div>
                <div id="ID_reporte_contenido">
                    <center>
                    <h2>Muertes promedio por casos confirmados y edad de covid 19 en un País</h2>
                    <p>
                    La evidencia acumulada sobre la COVID-19 ha mostrado que uno de los principales factores de riesgo de letalidad de esta patología corresponde a la edad (1,2). Como resultado, en la mayoría de los países de Europa occidental, únicamente el 5% de las personas fallecidas poseían edades inferiores a los 60 años.
                    </p>
                    <br/>
                    <p>
                       Cantidad de muertes promedio:<br/>
                       {contenido.promedio}<br/>
                    </p>                        
                    <p>   
                       Autor: Wilfred Stewart Perez Solorzano<br/>Carnet:201408419
                    </p>
                    </center>
                </div>
            </div>
    )
}

export default Reporte13;