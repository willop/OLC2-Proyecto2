import React from 'react'

const Reporte21=({contenido}) => {
    return(
        <div id="ID_reporte" >
                <div id="ID_imagen_reporte">

                    <center>
                    <h2>Porcentaje de hombres infectados por covid-19 en un País desde el primer caso activo</h2>
                        <h1>GRAFICA DE PREDICCION DE INFECTADOS</h1></center>                  
                    <center><img src={contenido.img}/>
                    <p>
                        Ecuacion polinomial de grado 2:<br/>
                       {contenido.ecuacion}<br/>
                       Coeficiente de determinacion(R^2):<br/>
                       {contenido.val_r_cuadrado}<br/>
                       Cantidad de muertes aproximadas son:<br/>
                       {contenido.aprox}<br/>
                    </p> 
                    </center>

                </div>
                <div id="ID_reporte_contenido">
                    <center>
                    
                    <br/>
                    <div id="ID_imagen_reporte">
                    <center><h1>GRAFICA DE PREDICCION DE MUERTES</h1></center>                  
                    <center><img src={contenido.img2}/></center>
                     </div>
                     <h2>Porcentaje de hombres infectados por covid-19 en un País desde el primer caso activo</h2>
                    <p>
                        Ecuacion polinomial de grado 2:<br/>
                       {contenido.ecuacion2}<br/>
                       Coeficiente de determinacion(R^2):<br/>
                       {contenido.val_r_cuadrado2}<br/>
                       Cantidad de muertes aproximadas son:<br/>
                       {contenido.aprox2}<br/>
                    </p>                        
                    <p>
                    Las vacunas para prevenir la enfermedad por coronavirus 2019 (COVID-19) tal vez sean la mejor esperanza para terminar con la pandemia. Sin embargo, mientras la Administración de Alimentos y Medicamentos (FDA, por sus siglas en inglés) siga aprobando o autorizando el uso de emergencia de las vacunas contra la COVID-19, es probable que sigas teniendo preguntas.
                    </p>
                    <p>   
                       Autor: Wilfred Stewart Perez Solorzano<br/>Carnet:201408419
                    </p>
                    </center>
                </div>
            </div>
    )
}

export default Reporte21;