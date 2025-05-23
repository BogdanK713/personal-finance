import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api';

const RegisterForm = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await api.post('/users/register', { username, email, password });
      navigate('/login');
    } catch (err) {
      alert('❌ Failed to register user.');
    }
  };

  return (
    <form onSubmit={handleRegister} style={styles.card}>
      <h2 style={styles.title}>📝 Register</h2>
      <input type="text" value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" required style={styles.input} />
      <input type="email" value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" required style={styles.input} />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" required style={styles.input} />
      <button type="submit" style={styles.button}>Register</button>
    </form>
  );
};

const styles = {
  card: { background: '#f4f4f4', padding: 24, borderRadius: 12, boxShadow: '0 2px 8px rgba(0,0,0,0.1)', display: 'flex', flexDirection: 'column', gap: 12, maxWidth: 400, margin: '0 auto' },
  title: { margin: 0, fontSize: 20, color: '#333', textAlign: 'center' },
  input: { padding: 10, fontSize: 16, borderRadius: 6, border: '1px solid #ccc' },
  button: { padding: 10, fontSize: 16, backgroundColor: '#007bff', color: '#fff', border: 'none', borderRadius: 6, cursor: 'pointer' }
};

export default RegisterForm;
