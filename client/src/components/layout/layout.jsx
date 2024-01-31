import React from 'react'
import Navbar from './navbar'
import Footer from './footer'


export default function Layout({children}) {
    return (
        <>
            <Navbar></Navbar>
            {children}
            <Footer></Footer>
        </>
        )
}

