import React, { useState, useEffect } from 'react';

export default function WeaponSelection({ selectedClass }) {
    const [weapons, setWeapons] = useState([]);

    const classWeapons = {
        Warrior: ['Longsword', 'Axe', 'Sword and Shield'],
        Mage: ['Staff', 'Wand', 'Magic Book'],
        Archer: ['Bow', 'Crossbow', 'Dagger'],
    };

    useEffect(() => {
        setWeapons(classWeapons[selectedClass] || []);
    }, [selectedClass]);

  return (
    <div className="px-3 inline-block relative w-64">
        <label className="block uppercase tracking-wide text-gray-200 text-xs font-bold my-2">
        Select Weapon
        </label>
        <select className="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-3 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline" >
            {weapons.map((weapon) => (
            <option key={weapon} value={weapon}>
                {weapon}
            </option>
            ))}
        </select>
    </div>
  )
}
