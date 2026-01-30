import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import SimpleDashboard from './pages/SimpleDashboard';
import SimpleEmployees from './pages/SimpleEmployees';
import Attendance from './pages/Attendance';
import LeaveManagement from './pages/LeaveManagement';
import ApiTest from './pages/ApiTest';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<SimpleDashboard />} />
          <Route path="/employees" element={<SimpleEmployees />} />
          <Route path="/attendance" element={<Attendance />} />
          <Route path="/leave-requests" element={<LeaveManagement />} />
          <Route path="/api-test" element={<ApiTest />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;