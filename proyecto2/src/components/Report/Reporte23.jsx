import React from 'react'

const Reporte23=({contenido}) => {
    return(
        <div id="ID_reporte" >
                <div id="ID_imagen_reporte">
                    <center><h1>GRAFICA SEGUN FACTOR DE MUERTE EN UN PAIS</h1></center>                  
                    <center><img src={contenido.img}/></center>
                </div>
            </div>
    )
}

export default Reporte23;