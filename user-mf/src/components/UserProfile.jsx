import React, { useEffect, useState } from 'react';
import api from '../api';
import { useAuth } from './AuthContext';

const UserProfile = () => {
  const { token, username, logout } = useAuth();
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    if (token) {
      api.get('/users/profile', { headers: { Authorization: `Bearer ${token}` } })
        .then(res => setProfile(res.data))
        .catch(err => {
          console.error('Failed to fetch profile:', err);
          logout();
        });
    }
  }, [token]);

  const deleteUser = async () => {
    if (window.confirm('Delete your account permanently?')) {
      try {
        await api.delete('/users/delete', { headers: { Authorization: `Bearer ${token}` } });
        alert('🗑️ Account deleted.');
        logout();
      } catch {
        alert('❌ Failed to delete user.');
      }
    }
  };

  if (!profile) return null;

  return (
    <div style={styles.card}>
      <h2 style={styles.title}>👤 Welcome, {profile.username}</h2>
      <p><strong>Email:</strong> {profile.email}</p>
      <div style={{ display: 'flex', gap: 10, marginTop: 12 }}>
        <button onClick={logout} style={{ ...styles.button, backgroundColor: '#6c757d' }}>🚪 Logout</button>
        <button onClick={deleteUser} style={{ ...styles.button, backgroundColor: '#dc3545' }}>🗑️ Delete</button>
      </div>
    </div>
  );
};

const styles = {
  card: { background: '#fff8dc', padding: 24, borderRadius: 12, boxShadow: '0 2px 8px rgba(0,0,0,0.1)', display: 'flex', flexDirection: 'column', gap: 10, maxWidth: 400, margin: '0 auto', textAlign: 'center' },
  title: { margin: 0, fontSize: 20, color: '#333' },
  button: { padding: 10, fontSize: 16, color: '#fff', border: 'none', borderRadius: 6, cursor: 'pointer', flex: 1 }
};

export default UserProfile;
