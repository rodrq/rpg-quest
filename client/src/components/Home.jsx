import React from 'react';
import GithubIcon from '../assets/github.svg';
import LinkedinIcon from '../assets/linkedin.svg';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="container mx-auto mt-8 px-10 py-5 text-gray-600 text-xl">
      <h1 className="text-3xl font-semibold mb-2">RPG Quest Generator</h1>
      <h2 className="text-2xl">
        Dynamic videogame quest generation using OpenAI's language model. 
      </h2>
      <p className="py-1">
        Generates personalized quests according to the context given. 
      </p>
      <p className="py-1">
        To start testing, create a character.
      </p>
      <p className="py-1">
        For more info, visit About page or <Link to="/about">Click here. </Link>
      </p>
      <div className='pt-10 flex items-baseline'>
        <a href="https://github.com/rodrq" target="_blank" rel="noopener noreferrer"><img className="w-16 h-w-16 mr-6" src={GithubIcon} alt="Github Icon" /></a>
        <a href="https://linkedin.com/in/rodrigo-rooney"target="_blank" rel="noopener noreferrer"><img className="w-16 h-w-16" src={LinkedinIcon} alt="Linkedin Icon" /></a>

      </div>

    </div>
  );
};

export default Home;
