import React from 'react'

import Navbar from '../components/layout/Navbar'
import Home from "../pages/public/Home"
import About from "../pages/public/About"
import { Routes, Route } from 'react-router-dom'
function App() {
  return (
    <>
    <main className='min-h-screen bg-slate-950 pt-5'>
      <Navbar/>
        <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/about" element={<About/>} />
        </Routes>
     
    </main>
    </>
  )
}

export default App