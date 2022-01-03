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
import  Consulta11  from '../pages/Consulta11';
import  Consulta12  from '../pages/Consulta12';
import  Consulta13  from '../pages/Consulta13';
import  Consulta14  from '../pages/Consulta14';
import  Consulta15  from '../pages/Consulta15';
import  Consulta16  from '../pages/Consulta16';
import  Consulta17  from '../pages/Consulta17';
import  Consulta18  from '../pages/Consulta18';
import  Consulta19  from '../pages/Consulta19';
import  Consulta20  from '../pages/Consulta20';
import  Consulta21  from '../pages/Consulta21';
import  Consulta22  from '../pages/Consulta22';
import  Consulta23  from '../pages/Consulta23';
import  Consulta24  from '../pages/Consulta24';
import  Consulta25  from '../pages/Consulta25';

export default function AppRouter() {
    return (
        /*<BrowserRouter>
      <Route path="/home" component={Barra_nav} >
      </Route>
    </BrowserRouter>*/
        <BrowserRouter>
        <Barra_nav/>
            <Routes>
                <Route path="./" element={<Lista_reportes/>} > </Route>
                <Route path="./carga_masiva" element={<Carga_archivo/>} > </Route>
                <Route path="./consulta1" element={<Consulta1/>} > </Route>
                <Route path="/consulta2" element={<Consulta2/>} > </Route>
                <Route path="/consulta3" element={<Consulta3/>} > </Route>
                <Route path="/consulta4" element={<Consulta4/>} > </Route>
                <Route path="/consulta5" element={<Consulta5/>} > </Route>
                <Route path="/consulta6" element={<Consulta6/>} > </Route>
                <Route path="/consulta7" element={<Consulta7/>} > </Route>
                <Route path="/consulta8" element={<Consulta8/>} > </Route>
                <Route path="/consulta9" element={<Consulta9/>} > </Route>
                <Route path="/consulta10" element={<Consulta10/>} > </Route>
                <Route path="/consulta11" element={<Consulta11/>} > </Route>
                <Route path="/consulta12" element={<Consulta12/>} > </Route>
                <Route path="/consulta13" element={<Consulta13/>} > </Route>
                <Route path="/consulta14" element={<Consulta14/>} > </Route>
                <Route path="/consulta15" element={<Consulta15/>} > </Route>
                <Route path="/consulta16" element={<Consulta16/>} > </Route>
                <Route path="/consulta17" element={<Consulta17/>} > </Route>
                <Route path="/consulta18" element={<Consulta18/>} > </Route>
                <Route path="/consulta19" element={<Consulta19/>} > </Route>
                <Route path="/consulta20" element={<Consulta20/>} > </Route>
                <Route path="/consulta21" element={<Consulta21/>} > </Route>
                <Route path="/consulta22" element={<Consulta22/>} > </Route>
                <Route path="/consulta23" element={<Consulta23/>} > </Route>
                <Route path="/consulta24" element={<Consulta24/>} > </Route>
                <Route path="/consulta25" element={<Consulta25/>} > </Route>
            </Routes>
        </BrowserRouter>
    )
}