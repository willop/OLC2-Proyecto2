import React from 'react'

const Reporte3=({contenido}) => {
    return(
        <div id="ID_reporte" >
                <div id="ID_imagen_reporte">
                    <center><h1>INDICE DE PROGRESION DE LA PANDEMIA</h1></center>
                    
                    <center><img src={contenido.img}/></center>
                </div>
                <div id="ID_reporte_contenido">
                    <center>
                    <h2>Indice de Progresión de la pandemia.</h2>
                    <p>
                    La subregión del Caribe y el Océano Atlántico sigue viendo una aceleración de los casos de COVID-19, y algunos países han declarado una quinta oleada de la pandemia en los últimos días. Entre los 36 países y territorios de la subregión, al menos la mitad de ellos han experimentado un aumento del 100% o más de casos durante los últimos 7 días en comparación con los 7 días anteriores (rango: 100% - 879%).
                    </p>
                    <br/>
                    <p>
                       La ecuacion de progresion lineal para este modelo es:<br/>
                       {contenido.ecuacion}<br/>
                       Coeficiente progresion es:<br/>
                       {contenido.mse}<br/>
                       Conclusion:<br/>
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

export default Reporte3;