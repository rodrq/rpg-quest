import React from 'react'

export default function Home() {
  return (
    <div className='flex flex-col  px-28 py-3 min-h-[85vh] text-gray-200'>
        <h1 className='text-center text-5xl py-3'>Dynamic RPG quest creator</h1>
        <h4 className='p-5 text-xl'> Cool little project to show what could be the future of online role playing games. With enough tuning, context and compatible graphic motor tools 
            it should be not so difficult for a language model to create fun and original missions for the player on real time. 
        </h4>
        <h4 className='p-5 text-xl'> This one's scope will be limited and small just to get the point across and to save money on infra costs. 
            We will create a typical RPG style character, select where we are at, and ChatGPT will create on the go a short mission
            for us. 
        </h4>
    </div>
  )
}
