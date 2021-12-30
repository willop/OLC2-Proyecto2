import React from 'react'

const Reporte=({contenido}) => {
    return(
        <div id="ID_reporte" >
                <div id="ID_imagen_reporte">
                    <center><h1>GRAFICA DE TENDENCIA</h1></center>
                    
                    <img src={contenido.img}/>
                </div>
                <div id="ID_reporte_contenido">
                    <p>
                        Una línea de tendencia lineal es una línea recta más adecuada que se usa con conjuntos de datos lineales sencillos. Los datos son lineales si el patrón en sus puntos de datos se parece a una línea. Una línea de tendencia lineal frecuentemente muestra que hay algo que aumenta o disminuye a un ritmo constante.
                    </p>
                </div>
            </div>
    )
}

export default Reporte;