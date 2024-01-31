import React from 'react'
import Form from './forms/charCreationForm'

export default function CreateCharacter() {
  return (
    <div className='min-h-[85vh]'>
    <div className=' text-center text-3xl text-gray-200 font-bold p-4'>
        Create your character 
    </div>
        <Form></Form>
    </div>
    
  )
}
