import React from 'react'
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className='flex p-4 pl-8 font-bold text-xl bg-[#0d2839] text-gray-200 '>
      <Link to='/'><img src="/swords-logo.svg" className='h-16 '></img></Link>
      <Link to='/'className='p-5 pl-7'>Home</Link>
      <Link to='/create' className='p-5'>Create character</Link>
    </nav>
  )
}
