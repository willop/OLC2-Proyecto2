import React from 'react'

const Reporte14=({contenido}) => {
    return(
        <div id="ID_reporte" >
                <div id="ID_imagen_reporte">
                    <center><h1>GRAFICA DE MUERTES POR REGION</h1></center>                  
                    <center><img src={contenido.img}/></center>
                </div>
                
            </div>
    )
}

export default Reporte14;