import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { AuthProvider } from './components/AuthContext';

import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';
import UserList from './components/UserList';
import UserProfile from './components/UserProfile';

const withProviders = (Component) => () => (
  <AuthProvider>
    <BrowserRouter>
      <Component />
    </BrowserRouter>
  </AuthProvider>
);

export const Login = withProviders(LoginForm);
export const Register = withProviders(RegisterForm);
export const Profile = withProviders(UserProfile);
export const Users = withProviders(UserList);

export { AuthProvider } from './components/AuthContext';
