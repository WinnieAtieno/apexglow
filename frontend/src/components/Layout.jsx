import React from 'react'
import { Outlet } from 'react-router-dom'
import Navbar from '../components/Navbar'

function Layout() {
  return (
    <main className='min-h-screen bg-sky-50 text-slate-900'>
        <Navbar/>
        <Outlet/>
    </main>
  )
}

export default Layout