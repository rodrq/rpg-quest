import React from 'react';
import { useHistory } from 'react-router-dom';

const CreatedQuest = ({ location }) => {

  const history = useHistory();
    
  const questResult = location.state?.questResult;

  if (!questResult) {
    return <p>No quest data available.</p>;
  }

  const handlePlayAgain = () => {
    history.replace('/play');
  };

  const handleQuests = () => {
    history.replace('/all_quests');
  };

  return (
    <div className='mx-auto max-w-7xl py-6 sm:px-6 lg:px-8'>
      <div className="container mt-10 bg-gray-200 p-10 rounded-lg">
        <h2 className="text-2xl font-bold mb-4 ">Quest Details</h2>
        <div className="mt-4">
          <p className='text-3xl font-bold  mb-2'>{questResult.quest.title}</p>
          <p className='text-lg font-bold mb-4'>{questResult.quest.description}</p>
          <p className='text-lg'>Rewards: {questResult.quest.rewards.join(', ')}</p>
          <p className='text-lg'>Experience: {questResult.quest.experience}</p>
        </div>
        <button onClick={handlePlayAgain} 
                className="bg-blue-600 text-white p-2 rounded-md mt-8 hover:bg-blue-600">
                Try Again
        </button>
        <button onClick={handleQuests} 
                className="bg-blue-500 text-white p-2 rounded-md mt-8 ml-2 hover:bg-blue-600">
                View quests
        </button>
        
      </div>
    </div>
  );
};

export default CreatedQuest;
