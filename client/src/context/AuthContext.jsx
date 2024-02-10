import React, { createContext, useContext, useState , useEffect} from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [authenticated, setAuthenticated] = useState(false);
  const [username, setUsername] = useState(null);

  
  const login = () => setAuthenticated(true);
  const logout = () => setAuthenticated(false);
  useEffect(() => {
    const checkCookies = () => {
      const cookies = document.cookie;
      if (cookies) {
        setAuthenticated(true);
      }
    };

    checkCookies();
  }, []);

  return (
    <AuthContext.Provider value={{ authenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
