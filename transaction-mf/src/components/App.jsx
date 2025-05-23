import React from 'react';
import TransactionList from './TransactionList';

const App = ({ token, user_id }) => {
  return <TransactionList token={token} user_id={user_id} />;
};

export default App;
