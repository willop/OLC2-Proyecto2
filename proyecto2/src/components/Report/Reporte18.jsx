import React from 'react'

const Reporte18=({contenido}) => {
    return(
        <div id="ID_reporte" >
                <div id="ID_imagen_reporte">
                    <center><h1>GRAFICA DE COMPORTAMIENTO Y CLASIFICACION</h1></center>                  
                    <center><img src={contenido.img}/></center>
                </div>
                <div id="ID_reporte_contenido">
                    <center>
                    <h2> Comportamiento y clasificación de personas infectadas por COVID-19 por municipio en un País.</h2>
                    <p>
                    Una vacuna contra la COVID-19 puede prevenir que tu hijo se contagie y que trasmita el virus que causa la COVID-19. Si tu hijo se contagia con la COVID-19, una vacuna contra la COVID-19 podría prevenir que se enferme de gravedad.<br/>Vacunarse contra la COVID-19 también le permitirá a tu hijo a comenzar a hacer las cosas que que quizás no pudo hacer durante la pandemia.
                    </p>
                    <br/>
                    <p>
                       Conclusion:<br/>
                       {contenido.conclusion}<br/>
                    </p>                        
                    <p>   
                       Autor: Wilfred Stewart Perez Solorzano<br/>Carnet:201408419
                    </p>
                    </center>
                </div>
            </div>
    )
}

export default Reporte18;