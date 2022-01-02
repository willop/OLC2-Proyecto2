import React from 'react'

const Reporte11=({contenido}) => {
    return(
        <div id="ID_reporte" >
                <div id="ID_imagen_reporte">
                    <center><h1>GRAFICA DE TENDENCIA DE INFECTADOS</h1></center>                  
                    <center><img src={contenido.img}/></center>
                </div>
                <div id="ID_reporte_contenido">
                    <center>
                    <h2>Tendencia de casos confirmados de Coronavirus en un departamento de un País.</h2>
                    <p>
                    Las vacunas para prevenir la enfermedad por coronavirus 2019 (COVID-19) tal vez sean la mejor esperanza para terminar con la pandemia. Sin embargo, mientras la Administración de Alimentos y Medicamentos (FDA, por sus siglas en inglés) siga aprobando o autorizando el uso de emergencia de las vacunas contra la COVID-19, es probable que sigas teniendo preguntas.
                    </p>
                    <br/>
                    <p>
                       Ecuacion del modelo de regresion polinomial grado 2:<br/>
                       {contenido.ecuacion}<br/>
                       Coeficiente de determinacion(R^2):<br/>
                       {contenido.r_cuadrado}<br/>
                       Error cuadratico medio(RMSE):<br/>
                       {contenido.mse}<br/>
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