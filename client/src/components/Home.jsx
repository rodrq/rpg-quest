import React from 'react';
import GithubIcon from '../assets/github.svg';
import LinkedinIcon from '../assets/linkedin.svg';


const Home = () => {
  return (
    <div className="container mx-auto mt-8 px-10 py-5 text-gray-600 text-xl">
      <h2 className="text-3xl font-semibold mb-4">Welcome to RPG Quest Generator</h2>
      <p className="py-1">
        Test a basic version of what I believe is the future of MMORPGs. 
      </p>
      <p className="pt-1">
        AI dynamic quest generation with the proper implementation and resources is going to be a game changer. 
      </p>
      <p className="">
        For more info, visit About page. 
      </p>
      <p className="py-1">
        This proof of concept was done with OpenAI API, FastAPI and React.
      </p>
      <div className='pt-10 flex items-baseline'>
        <a href="https://github.com/rodrq" target="_blank" rel="noopener noreferrer"><img className="w-16 h-w-16 mr-6" src={GithubIcon} alt="Github Icon" /></a>
        <a href="https://linkedin.com/in/rodrigo-rooney"target="_blank" rel="noopener noreferrer"><img className="w-16 h-w-16" src={LinkedinIcon} alt="Linkedin Icon" /></a>

      </div>

    </div>
  );
};

export default Home;
