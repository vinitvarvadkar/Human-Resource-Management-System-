import React, { useState, useEffect } from 'react';
import { employeeApi, dashboardApi } from '../services/api';

const SimpleDashboard: React.FC = () => {
  const [employees, setEmployees] = useState<any[]>([]);
  const [stats, setStats] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        console.log('Fetching data...');
        const [employeesData, statsData] = await Promise.all([
          employeeApi.getAll(),
          dashboardApi.getStats()
        ]);
        
        console.log('Employees:', employeesData);
        console.log('Stats:', statsData);
        
        setEmployees(employeesData);
        setStats(statsData);
        setError(null);
      } catch (err: any) {
        console.error('Error fetching data:', err);
        setError(err.message || 'Failed to fetch data');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="p-8">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4">Loading...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-8">
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
          <strong>Error:</strong> {error}
        </div>
      </div>
    );
  }

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">HRMS Dashboard</h1>
      
      {/* Stats Cards */}
      {stats && (
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-700">Total Employees</h3>
            <p className="text-3xl font-bold text-blue-600">{stats.total_employees}</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-700">Present Today</h3>
            <p className="text-3xl font-bold text-green-600">{stats.present_today}</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-700">Absent Today</h3>
            <p className="text-3xl font-bold text-red-600">{stats.absent_today}</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-700">Attendance Rate</h3>
            <p className="text-3xl font-bold text-purple-600">{stats.average_attendance_rate}%</p>
          </div>
        </div>
      )}

      {/* Employees List */}
      <div className="bg-white rounded-lg shadow">
        <div className="px-6 py-4 border-b">
          <h2 className="text-xl font-semibold">Employees ({employees.length})</h2>
        </div>
        <div className="p-6">
          {employees.length === 0 ? (
            <p className="text-gray-500">No employees found</p>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {employees.map((employee) => (
                <div key={employee.id} className="border rounded-lg p-4">
                  <h3 className="font-semibold">{employee.full_name}</h3>
                  <p className="text-sm text-gray-600">{employee.employee_id}</p>
                  <p className="text-sm text-gray-600">{employee.department}</p>
                  <p className="text-sm text-gray-600">{employee.email}</p>
                  <span className={`inline-block px-2 py-1 text-xs rounded-full mt-2 ${
                    employee.status === 'Active' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
                  }`}>
                    {employee.status}
                  </span>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default SimpleDashboard;