import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Barra_nav } from '../components/Barra_nav';
import { Carga_archivo} from '../pages/Carga_archivo';
import { Lista_reportes} from '../components/Lista_reportes';
import  Consulta1  from '../pages/Consulta1';
import  Consulta2  from '../pages/Consulta2';
import  Consulta3  from '../pages/Consulta3';
import  Consulta4  from '../pages/Consulta4';
import  Consulta5  from '../pages/Consulta5';
import  Consulta6  from '../pages/Consulta6';
import  Consulta7  from '../pages/Consulta7';
import  Consulta8  from '../pages/Consulta8';
import  Consulta9  from '../pages/Consulta9';
import  Consulta10  from '../pages/Consulta10';

export default function AppRouter() {
    return (
        /*<BrowserRouter>
      <Route path="/home" component={Barra_nav} >
      </Route>
    </BrowserRouter>*/
        <BrowserRouter>
        <Barra_nav/>
            <Routes>
                <Route path="/" element={<Lista_reportes/>} > </Route>
                <Route path="/carga_masiva" element={<Carga_archivo/>} > </Route>
                <Route path="/consulta1" element={<Consulta1/>} > </Route>
                <Route path="/consulta2" element={<Consulta2/>} > </Route>
                <Route path="/consulta3" element={<Consulta3/>} > </Route>
                <Route path="/consulta4" element={<Consulta4/>} > </Route>
                <Route path="/consulta5" element={<Consulta5/>} > </Route>
                <Route path="/consulta6" element={<Consulta6/>} > </Route>
                <Route path="/consulta7" element={<Consulta7/>} > </Route>
                <Route path="/consulta8" element={<Consulta8/>} > </Route>
                <Route path="/consulta9" element={<Consulta9/>} > </Route>
                <Route path="/consulta10" element={<Consulta10/>} > </Route>
                <Route path="/consulta11" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta12" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta13" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta14" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta15" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta16" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta17" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta18" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta19" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta20" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta21" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta22" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta23" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta24" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta25" element={<h1>Hola mundo</h1>} > </Route>
            </Routes>
        </BrowserRouter>
    )
}