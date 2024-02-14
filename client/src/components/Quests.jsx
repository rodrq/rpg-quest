import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
const getCookie = (name) => {
  const cookies = document.cookie.split(';');
  for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i].trim();
    if (cookie.startsWith(`${name}=`)) {
      return cookie.substring(name.length + 1);
    }
  }
  return null;
};

const Quests = () => {
  const apiUrl = process.env.REACT_APP_API_URL;

  const [quests, setQuests] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchQuests = async () => {
      try {
        const accessToken = getCookie('token');

        const response = await fetch(apiUrl + 'quest/all', {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });

        if (response.ok) {
          const questsData = await response.json();
          setQuests(questsData);
        } else {
          console.error('Failed to fetch quests:', response.statusText);
        }
      } catch (error) {
        console.error('Error during quest fetch:', error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchQuests();
  }, []);

  if (loading) {
    return <p>Loading quests...</p>;
  }

  return (
    <div className="container mx-auto mt-8 px-10 py-5 text-gray-600 text-xl">
      <h2 className="text-2xl font-bold mb-4">All Quests</h2>
      {quests && quests.length > 0 ? (
        quests.map((quest) => (
          <div key={quest.quest_id} className="mb-4">
            <Link to={`/quest/${quest.quest_id}`}>
              <p className="text-lg font-bold">{quest.title}</p>
            </Link>
          </div>
        ))
      ) : (
        <div>
          <p>No quests available.</p>
          <Link to='/play'>Click here to create one</Link>
        </div>
      )}
    </div>
  );
};

export default Quests;
