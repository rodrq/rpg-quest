import React, { useState } from 'react'


export default function CreateCharacterForm() {
  
    const [formData, setFormData] = useState({
      name: '',
      password: '',
      rpgClass: 'none',
    });
  
    const handleInputChange = (e) => {
      const { name, value } = e.target;
      setFormData({
        ...formData,
        [name]: value,
      });
    };
  
    const handleSubmit = (e) => {
      e.preventDefault();
      console.log('Created char ' + formData.name);
    }

  return (
    <form onSubmit={handleSubmit} className='min-h-[85vh]'>
      <div className=' text-center text-3xl text-gray-200 font-bold p-4'>
          Create your character 
      </div>
      <div className="w-full md:w-1/2 px-3 mb-6 md:mb-0">
        <label className="block uppercase tracking-wide text-gray-200 text-xs font-bold mb-2">
            Name
        </label>
        <input type="text" name="name" value={formData.name} onChange={handleInputChange} className="appearance-none block w-full bg-gray-200 text-gray-800 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"/>
      </div>
      <div className="w-full md:w-1/2 px-3 mb-6 md:mb-0">
        <label className="block uppercase tracking-wide text-gray-200 text-xs font-bold mb-2">
            Password
        </label>
        <input type="password" name="password" value={formData.password} onChange={handleInputChange} className="appearance-none block w-full bg-gray-200 text-gray-800 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"/>
      </div>
      <div className="px-3 inline-block relative w-64">
        <label className="block uppercase tracking-wide text-gray-200 text-xs font-bold mb-2">
          Select Class
        </label>
        <select type="text" name="rpgClass" value={formData.rpgClass} onChange={handleInputChange} className="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-3 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline">
         <option value="none" className='disabled hidden'>-</option>
          <option value="warrior">Warrior</option>
          <option value="mage">Mage</option>
          <option value="cleric">Cleric</option>
          <option value="archer">Archer</option> 
        </select>
      </div>
      <button type="submit" className='rounded bg-yellow-200 p-2'>Create</button>    
    </form>
  )
}
