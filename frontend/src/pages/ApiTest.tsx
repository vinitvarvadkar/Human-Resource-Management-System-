import React, { useState, useEffect } from 'react';
import { employeeApi } from '../services/api';

const ApiTest: React.FC = () => {
  const [status, setStatus] = useState('Testing...');
  const [employees, setEmployees] = useState<any[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const testApi = async () => {
      try {
        setStatus('Fetching employees...');
        const data = await employeeApi.getAll();
        setEmployees(data);
        setStatus(`Success! Found ${data.length} employees`);
        setError(null);
      } catch (err: any) {
        console.error('API Error:', err);
        setError(err.message || 'Unknown error');
        setStatus('Failed to fetch employees');
      }
    };

    testApi();
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">API Connection Test</h1>
      
      <div className="mb-4">
        <strong>Status:</strong> {status}
      </div>
      
      {error && (
        <div className="mb-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded">
          <strong>Error:</strong> {error}
        </div>
      )}
      
      <div className="mb-4">
        <strong>API Base URL:</strong> {process.env.REACT_APP_API_URL || 'http://localhost:8000'}
      </div>
      
      {employees.length > 0 && (
        <div>
          <h2 className="text-xl font-semibold mb-2">Employees Found:</h2>
          <ul className="list-disc pl-5">
            {employees.map((emp: any) => (
              <li key={emp.id}>
                {emp.employee_id} - {emp.full_name} ({emp.department})
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default ApiTest;