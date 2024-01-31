import React, { useState } from 'react'
import WeaponSelection from './weaponSelection'
import ClassSelection from './classSelection'
import Input from './input'



export default function CreateCharacterForm() {
  const [selectedClass, setSelectedClass] = useState('');
  const handleClassSelect = (selectedClass) => {
    setSelectedClass(selectedClass);
  }; 

  
  return (
    <form className='min-h-[85vh]'>
      <div className=' text-center text-3xl text-gray-200 font-bold p-4'>
          Create your character 
      </div>
      <Input label="Name" type="text" id="name"/>
      <Input label="Password" type="password" id="password"/>
      <ClassSelection onSelectClass={handleClassSelect} />
      <WeaponSelection selectedClass={selectedClass}/>
      <button type="submit">Submit</button>
      
    </form>
    
  )
}
