import React from 'react';

export default function ClassSelection({ onSelectClass }) {
    const classes = ['Warrior', 'Mage', 'Archer'];

    const handleClassChange = (e) => {
        const selectedClass = e.target.value;
        onSelectClass(selectedClass);
      };
    return (
        <div className="px-3 inline-block relative w-64">
            <label className="block uppercase tracking-wide text-gray-200 text-xs font-bold mb-2">
            Select Class
            </label>
            <select onChange={handleClassChange} className="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-3 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline">
                <option value="">Select</option>
                {classes.map((characterClass) => (
                <option key={characterClass} value={characterClass}>
                    {characterClass}
                </option>
                ))}
            </select>
        </div>
  )
}
