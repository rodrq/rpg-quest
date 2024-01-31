import React from 'react'

export default function Input({ label, type, id, placeholder }) {
  return (
    <div className="w-full md:w-1/2 px-3 mb-6 md:mb-0">
        <label htmlFor={id} className="block uppercase tracking-wide text-gray-200 text-xs font-bold mb-2">
            {label}
        </label>
        <input
            id={id}
            type={type}
            className="appearance-none block w-full bg-gray-200 text-gray-800 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
            placeholder={placeholder}
        />
    </div>
  )
}
