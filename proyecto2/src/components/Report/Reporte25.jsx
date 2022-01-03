import React from 'react'

const Reporte25=({contenido}) => {
    return(
        <div id="ID_reporte" >
                <div id="ID_imagen_reporte">
                    <center><h1>GRAFICA DE PREDICCION DE MUERTES EN UN AÑO</h1></center>
                    
                    <center><img src={contenido.img}/></center>
                </div>
                <div id="ID_reporte_contenido">
                    <center>
                    <h2>Predicción de casos de un país para un año.</h2>
                    <p>
                    La subregión del Caribe y el Océano Atlántico sigue viendo una aceleración de los casos de COVID-19, y algunos países han declarado una quinta oleada de la pandemia en los últimos días. Entre los 36 países y territorios de la subregión, al menos la mitad de ellos han experimentado un aumento del 100% o más de casos durante los últimos 7 días en comparación con los 7 días anteriores (rango: 100% - 879%).
                    </p>
                    <br/>
                    <p>
                       Ecuacion polinomial de grado 2:<br/>
                       {contenido.mse}<br/>
                       Coeficiente de determinacion(R^2):<br/>
                       {contenido.val_r_cuadrado}<br/>
                       Cantidad de muertes aproximadas son:<br/>
                       {contenido.aprox}<br/>
                       <br/>
                       <br/>
                       Autor: Wilfred Stewart Perez Solorzano<br/>Carnet:201408419
                    </p>
                    </center>
                </div>
            </div>
    )
}

export default Reporte25;


