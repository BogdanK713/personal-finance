import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api';
import { useAuth } from './AuthContext';

const LoginForm = () => {
  const { login } = useAuth();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const form = new URLSearchParams();
      form.append('username', username);
      form.append('password', password);

      const res = await api.post('/users/login', form, {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      });

      const token = res.data.access_token;
      const user_id = res.data.user_id; // ✅ make sure this is returned by backend

      // Set in context and localStorage
      login(token, username);
      localStorage.setItem('token', token);
      localStorage.setItem('user', JSON.stringify({ id: user_id, username }));

      navigate('/profile');
    } catch (err) {
      alert('❌ Invalid username or password.');
    }
  };

  return (
    <form onSubmit={handleLogin} style={styles.card}>
      <h2 style={styles.title}>🔐 Login</h2>
      <input type="text" value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" required style={styles.input} />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" required style={styles.input} />
      <button type="submit" style={styles.button}>Login</button>
    </form>
  );
};

const styles = {
  card: {
    background: '#f4f4f4',
    padding: 24,
    borderRadius: 12,
    boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
    display: 'flex',
    flexDirection: 'column',
    gap: 12,
    maxWidth: 400,
    margin: '0 auto'
  },
  title: { margin: 0, fontSize: 20, color: '#333', textAlign: 'center' },
  input: { padding: 10, fontSize: 16, borderRadius: 6, border: '1px solid #ccc' },
  button: { padding: 10, fontSize: 16, backgroundColor: '#28a745', color: '#fff', border: 'none', borderRadius: 6, cursor: 'pointer' }
};

export default LoginForm;
