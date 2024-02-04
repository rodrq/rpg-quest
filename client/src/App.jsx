import React from 'react'
import {
  Routes,
  Route,
} from "react-router-dom";

import Layout from './components/layout/layout';
import Home from './components/home';
import ErrorPage from './components/errorPage';
import CreateCharacterForm from './components/createCharacterForm';

function App() {
  return (
    <>
      <Layout>
        <Routes>
          <Route path='*' element={<ErrorPage/>} />
          <Route path='/' element={<Home/>}></Route>
          <Route path='/create' element={<CreateCharacterForm/>}></Route>
        </Routes>
      </Layout>
    </>
    )
}

export default App
