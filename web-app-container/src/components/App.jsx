import React, { lazy, Suspense } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";

import Navigation from "./Navigation";

// Remote components
const Login = lazy(() => import("userApp/Login").then(m => ({ default: m.Login })));
const Register = lazy(() => import("userApp/Register").then(m => ({ default: m.Register })));
const Profile = lazy(() => import("userApp/Profile").then(m => ({ default: m.Profile })));
const UserList = lazy(() => import("userApp/Users").then(m => ({ default: m.Users })));
const AnalyticsApp = lazy(() => import("analyticsApp/AnalyticsApp"));
const TransactionList = lazy(() => import("transactionApp/TransactionList"));

// Auth context
import { AuthProvider, useAuth } from "userApp/AuthContext";

const ProtectedRoute = ({ children }) => {
  const { token } = useAuth();
  return token ? children : <Navigate to="/login" replace />;
};

const AppRoutes = () => {
  const { token } = useAuth();
  const userData = JSON.parse(localStorage.getItem("user") || "{}");

  return (
    <div className="max-w-6xl mx-auto px-4">
      <Navigation />
      <main className="py-6">
        <Suspense fallback={<div>Loading...</div>}>
          <Routes>
            <Route path="/" element={<Navigate to="/login" />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route
              path="/profile"
              element={
                <ProtectedRoute>
                  <Profile />
                </ProtectedRoute>
              }
            />
            <Route
              path="/users"
              element={
                <ProtectedRoute>
                  <UserList />
                </ProtectedRoute>
              }
            />
            <Route
              path="/transactions"
              element={
                <ProtectedRoute>
                  <TransactionList token={token} user_id={userData.id} />
                </ProtectedRoute>
              }
            />
            <Route
              path="/analytics"
              element={
                <ProtectedRoute>
                  <AnalyticsApp token={token} user_id={userData.id} />
                </ProtectedRoute>
              }
            />
          </Routes>
        </Suspense>
      </main>
    </div>
  );
};

const App = () => {
  return (
    <AuthProvider>
      <Router>
        <div className="flex flex-col min-h-screen bg-gray-50">
          <AppRoutes />
        </div>
      </Router>
    </AuthProvider>
  );
};

export default App;
