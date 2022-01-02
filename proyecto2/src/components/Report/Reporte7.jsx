import React from 'react'

const Reporte7=({contenido}) => {
    return(
        <div id="ID_reporte" >
                <div id="ID_imagen_reporte">
                    <center><h1>GRAFICA DE TENDENCIA DIARIA</h1></center>
                    
                    <center><img src={contenido.img}/></center>
                </div>
                <div id="ID_reporte_contenido">
                    <center>
                    <h2>Tendencia de la infección por Covid-19 en un País</h2>
                    <p>
                    La subregión del Caribe y el Océano Atlántico sigue viendo una aceleración de los casos de COVID-19, y algunos países han declarado una quinta oleada de la pandemia en los últimos días. Entre los 36 países y territorios de la subregión, al menos la mitad de ellos han experimentado un aumento del 100% o más de casos durante los últimos 7 días en comparación con los 7 días anteriores (rango: 100% - 879%).
                    </p>
                    <br/>
                    <p>
                       Ecuacion del modelo de regresion lineal:<br/>
                       {contenido.ecuacion}<br/>
                       Coeficiente de determinacion(R^2):<br/>
                       {contenido.val_r_cuadrado}<br/>
                       5 Aproximaciones posteriores utilizando la ecuacion:<br/>
                       {contenido.aproximaciones}<br/>
                    </p>
                    <div>
                    <br/>
                       <center><h1>Media de fectados diarios</h1><br/>
                       <img src={contenido.img2}/></center>
                       <br/>
                    </div>
                        
                    <p>   
                       Autor: Wilfred Stewart Perez Solorzano<br/>Carnet:201408419
                    </p>
                    </center>
                </div>
            </div>
    )
}

export default Reporte7;