import React, { useState } from 'react';



export default function CreateCharacter() {

  const [selectedClass, setSelectedClass] = useState('');
  const [weapons, setWeapons] = useState([]);

  // Define classes and their respective weapons
  const classWeapons = {
    warrior: ['Longsword', 'Axe', 'Sword and Shield'],
    mage: ['Staff', 'Wand', 'Magic Book'],
    archer: ['Bow', 'Crossbow', 'Dagger'],
  };
  const handleClassChange = (e) => {
    const selectedClass = e.target.value;
    setSelectedClass(selectedClass);

    // Update weapons based on the selected class
    setWeapons(classWeapons[selectedClass] || []);
  };

  return (
    <div className='min-h-[85vh]'>
      <div className=' text-center text-3xl text-gray-200 font-bold'>
        Create your character 
      </div>
      <div className="w-full md:w-1/2 px-3 mb-6 md:mb-0">
        <label className="block uppercase tracking-wide text-gray-200 text-xs font-bold mb-2">
          Name
        </label>
        <input className="appearance-none block w-full bg-gray-200 text-gray-800 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" id="grid-first-name" type="text"></input>
      </div>
      <div className="w-full md:w-1/2 px-3 mb-6 md:mb-0">
        <label className="block uppercase tracking-wide text-gray-200 text-xs font-bold mb-2">
          Password
        </label>
        <input className="appearance-none block w-full bg-gray-200 text-gray-800 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" id="grid-first-name" type="password"></input>
      </div>
      <div className="px-3 inline-block relative w-64">
        <label className="block uppercase tracking-wide text-gray-200 text-xs font-bold mb-2">
          Select Class
        </label>
          <select value={selectedClass} onChange={handleClassChange} className="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-3 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline">
            <option value='select'>Select</option>
            <option value="warrior">Warrior</option>
            <option value="mage">Mage</option>
            <option value="archer">Archer</option>
          </select>
        </div>
        <div className="px-3 inline-block relative w-64">
        <label className="block uppercase tracking-wide text-gray-200 text-xs font-bold my-2 ">
          Select Weapon
        </label>
        { 
          <select className="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-3 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline" >
            {weapons.map((weapon) => (
              <option key={weapon} value={weapon}>
                {weapon}
              </option>
              ))}
            </select>
          
      }
      </div>  
      <div className='px-3 pt-4'>
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Create
        </button>
      </div>
    </div>
    

  )
}
