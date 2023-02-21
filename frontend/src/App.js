import React from 'react';
import {Coffee} from "./components/Coffee";
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import {CoffeeCreate} from "./components/CoffeeCreate";
import {Orders} from "./components/Orders";

function App() {
    return <BrowserRouter>
        <Routes>
            <Route path="/" element={<Coffee/>}/>
            <Route path="/create" element={<CoffeeCreate/>}/>
            <Route path="/orders" element={<Orders/>}/>
        </Routes>
    </BrowserRouter>;
}

export default App;
