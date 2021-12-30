import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Barra_nav } from '../components/Barra_nav';
import { Carga_archivo} from '../pages/Carga_archivo';
import { Lista_reportes} from '../components/Lista_reportes';
import  Consulta1  from '../pages/Consulta1';

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
                <Route path="/consulta2" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta3" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta4" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta5" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta6" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta7" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta8" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta9" element={<h1>Hola mundo</h1>} > </Route>
                <Route path="/consulta10" element={<h1>Hola mundo</h1>} > </Route>
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