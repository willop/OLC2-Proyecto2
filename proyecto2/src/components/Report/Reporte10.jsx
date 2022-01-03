import React from 'react'

const Reporte10=({contenido}) => {
    return(
        <div id="ID_reporte" >
                <div id="ID_imagen_reporte">
                    <center><h1>GRAFICA DE COMPARACION DE VACUNACION POR PAIS.</h1></center>
                    
                    <center><img src={contenido.img}/></center>
                </div>
                <div id="ID_reporte_contenido">
                    <center>
                    <h2>Analisis comparativo de vacunacion entre 2 paises.</h2>
                    <br/>
                    
                     <h2>Informacion del primer pais</h2>
                     <p>
                       Ecuacion del modelo de regresion polinomial de grado 2:<br/>
                       {contenido.ecuacion}<br/>
                       Coeficiente de determinacion(R^2):<br/>
                       {contenido.r_cuadrado}<br/>
                       Error cuadratico medio:<br/>
                       {contenido.mse}<br/>
                       <br/>
                    </p>
                    <h2>Informacion del segundo pais</h2>
                    <p>
                       
                       Ecuacion del modelo de regresion polinomial de grado 2:<br/>
                       {contenido.ecuacion2}<br/>
                       Coeficiente de determinacion(R^2):<br/>
                       {contenido.r_cuadrado2}<br/>
                       Error cuadratico medio:<br/>
                       {contenido.mse2}<br/>
                       <br/>
                       <br/>
                       Conclusion:<br/>
                       {contenido.conclusion}
                       <br/>
                       <br/>
                       <br/>
                       Autor: Wilfred Stewart Perez Solorzano<br/>Carnet:201408419
                    </p>
                    </center>
                </div>
            </div>
    )
}

export default Reporte10;