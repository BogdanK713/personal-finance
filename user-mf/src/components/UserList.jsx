import React, { useEffect, useState } from 'react';
import api from '../api';

const UserList = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    api.get('/users').then(res => setUsers(res.data)).catch(console.error);
  }, []);

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>📋 Registered Users</h2>
      <ul style={styles.list}>
        {users.map((user, idx) => (
          <li key={idx} style={styles.item}><strong>{user.username}</strong> — <em>{user.email}</em></li>
        ))}
      </ul>
    </div>
  );
};

const styles = {
  container: { marginTop: 32, padding: 20, background: '#fff', borderRadius: 12, boxShadow: '0 1px 4px rgba(0,0,0,0.1)' },
  title: { marginBottom: 12, fontSize: 18, color: '#333' },
  list: { listStyle: 'none', paddingLeft: 0 },
  item: { padding: '8px 0', borderBottom: '1px solid #eee' }
};

export default UserList;
