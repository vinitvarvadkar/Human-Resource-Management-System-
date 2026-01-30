import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { dashboardApi, employeeApi, attendanceApi } from '../services/api';
import { DashboardStats, DepartmentStats, Employee, AttendanceRecord } from '../types';
import LoadingSpinner from '../components/LoadingSpinner';
import ErrorMessage from '../components/ErrorMessage';

const Dashboard: React.FC = () => {
  const [stats, setStats] = useState<DashboardStats | null>(null);
  const [departmentStats, setDepartmentStats] = useState<DepartmentStats[]>([]);
  const [recentEmployees, setRecentEmployees] = useState<Employee[]>([]);
  const [recentAttendance, setRecentAttendance] = useState<AttendanceRecord[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchData = async () => {
    try {
      setLoading(true);
      setError(null);
      const [statsData, deptStatsData, employeesData, attendanceData] = await Promise.all([
        dashboardApi.getStats(),
        dashboardApi.getDepartmentStats(),
        employeeApi.getAll(),
        attendanceApi.getAll()
      ]);
      
      setStats(statsData);
      setDepartmentStats(deptStatsData);
      setRecentEmployees(employeesData.slice(0, 5));
      setRecentAttendance(attendanceData.slice(0, 10));
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to fetch dashboard data');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <LoadingSpinner size="lg" />
      </div>
    );
  }

  if (error) {
    return <ErrorMessage message={error} onRetry={fetchData} />;
  }

  if (!stats) {
    return <div>No data available</div>;
  }

  const quickStats = [
    {
      title: 'Total Employees',
      value: stats.total_employees,
      icon: '👥',
      color: 'bg-blue-500',
      link: '/employees',
      change: '+12%',
      changeType: 'positive'
    },
    {
      title: 'Present Today',
      value: stats.present_today,
      icon: '✅',
      color: 'bg-green-500',
      link: '/attendance',
      change: `${stats.average_attendance_rate}%`,
      changeType: 'neutral'
    },
    {
      title: 'Absent Today',
      value: stats.absent_today,
      icon: '❌',
      color: 'bg-red-500',
      link: '/attendance',
      change: '-5%',
      changeType: 'positive'
    },
    {
      title: 'Pending Leaves',
      value: stats.pending_leave_requests,
      icon: '📋',
      color: 'bg-yellow-500',
      link: '/leave-requests',
      change: '+3',
      changeType: 'negative'
    },
    {
      title: 'Departments',
      value: stats.departments_count,
      icon: '🏢',
      color: 'bg-purple-500',
      link: '/departments',
      change: 'Stable',
      changeType: 'neutral'
    },
    {
      title: 'Monthly Payroll',
      value: `$${stats.total_payroll_this_month.toLocaleString()}`,
      icon: '💰',
      color: 'bg-indigo-500',
      link: '/payroll',
      change: '+8%',
      changeType: 'positive'
    }
  ];

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
          <p className="mt-2 text-gray-600">Welcome to HRMS Lite - Your comprehensive HR solution</p>
        </div>
        <div className="flex space-x-3">
          <button className="btn-secondary">
            📊 Generate Report
          </button>
          <button className="btn-primary">
            ➕ Quick Add
          </button>
        </div>
      </div>

      {/* Quick Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-6">
        {quickStats.map((stat, index) => (
          <Link
            key={index}
            to={stat.link}
            className="card hover:shadow-lg transition-all duration-200 cursor-pointer transform hover:-translate-y-1"
          >
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">{stat.title}</p>
                <p className="text-2xl font-bold text-gray-900 mt-1">{stat.value}</p>
                <div className="flex items-center mt-2">
                  <span className={`text-xs font-medium ${
                    stat.changeType === 'positive' ? 'text-green-600' :
                    stat.changeType === 'negative' ? 'text-red-600' : 'text-gray-600'
                  }`}>
                    {stat.change}
                  </span>
                </div>
              </div>
              <div className={`${stat.color} p-3 rounded-lg text-white text-2xl`}>
                {stat.icon}
              </div>
            </div>
          </Link>
        ))}
      </div>

      {/* Charts and Analytics Row */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Attendance Overview */}
        <div className="card">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Attendance Overview</h2>
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <span className="text-sm font-medium text-gray-600">Overall Attendance Rate</span>
              <span className="text-lg font-bold text-green-600">{stats.average_attendance_rate}%</span>
            </div>
            
            {/* Simple Progress Bar */}
            <div className="w-full bg-gray-200 rounded-full h-3">
              <div 
                className="bg-green-500 h-3 rounded-full transition-all duration-500"
                style={{ width: `${stats.average_attendance_rate}%` }}
              ></div>
            </div>
            
            <div className="grid grid-cols-2 gap-4 mt-4">
              <div className="text-center p-3 bg-green-50 rounded-lg">
                <div className="text-2xl font-bold text-green-600">{stats.present_today}</div>
                <div className="text-sm text-gray-600">Present Today</div>
              </div>
              <div className="text-center p-3 bg-red-50 rounded-lg">
                <div className="text-2xl font-bold text-red-600">{stats.absent_today}</div>
                <div className="text-sm text-gray-600">Absent Today</div>
              </div>
            </div>
          </div>
        </div>

        {/* Department Performance */}
        <div className="card">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Department Performance</h2>
          <div className="space-y-3">
            {departmentStats.slice(0, 5).map((dept, index) => (
              <div key={index} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                <div>
                  <div className="font-medium text-gray-900">{dept.department}</div>
                  <div className="text-sm text-gray-600">{dept.total_employees} employees</div>
                </div>
                <div className="text-right">
                  <div className="font-bold text-gray-900">{dept.attendance_rate}%</div>
                  <div className="text-sm text-gray-600">Attendance</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Recent Activity Row */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Recent Employees */}
        <div className="card">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-xl font-semibold text-gray-900">Recent Employees</h2>
            <Link to="/employees" className="text-primary-600 hover:text-primary-700 font-medium text-sm">
              View All →
            </Link>
          </div>
          <div className="space-y-3">
            {recentEmployees.map((employee) => (
              <div key={employee.id} className="flex items-center space-x-3 p-3 hover:bg-gray-50 rounded-lg">
                <div className="w-10 h-10 bg-primary-100 rounded-full flex items-center justify-center">
                  <span className="text-primary-600 font-medium">
                    {employee.full_name.charAt(0)}
                  </span>
                </div>
                <div className="flex-1">
                  <div className="font-medium text-gray-900">{employee.full_name}</div>
                  <div className="text-sm text-gray-600">{employee.department} • {employee.employee_id}</div>
                </div>
                <span className={`px-2 py-1 text-xs font-semibold rounded-full ${
                  employee.status === 'Active' ? 'bg-green-100 text-green-800' :
                  employee.status === 'Inactive' ? 'bg-yellow-100 text-yellow-800' :
                  'bg-red-100 text-red-800'
                }`}>
                  {employee.status}
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* Recent Attendance */}
        <div className="card">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-xl font-semibold text-gray-900">Recent Attendance</h2>
            <Link to="/attendance" className="text-primary-600 hover:text-primary-700 font-medium text-sm">
              View All →
            </Link>
          </div>
          <div className="space-y-3">
            {recentAttendance.map((record) => (
              <div key={record.id} className="flex items-center justify-between p-3 hover:bg-gray-50 rounded-lg">
                <div>
                  <div className="font-medium text-gray-900">{record.employee_name || record.employee_id}</div>
                  <div className="text-sm text-gray-600">{new Date(record.date).toLocaleDateString()}</div>
                </div>
                <div className="flex items-center space-x-2">
                  {record.check_in_time && (
                    <span className="text-xs text-gray-500">{record.check_in_time}</span>
                  )}
                  <span className={`px-2 py-1 text-xs font-semibold rounded-full ${
                    record.status === 'Present' ? 'bg-green-100 text-green-800' :
                    record.status === 'Late' ? 'bg-yellow-100 text-yellow-800' :
                    record.status === 'Half Day' ? 'bg-blue-100 text-blue-800' :
                    'bg-red-100 text-red-800'
                  }`}>
                    {record.status}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="card">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">Quick Actions</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <Link
            to="/employees"
            className="flex items-center p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors duration-200"
          >
            <span className="text-2xl mr-3">👤</span>
            <div>
              <h3 className="font-medium text-gray-900">Add Employee</h3>
              <p className="text-sm text-gray-600">Register new team member</p>
            </div>
          </Link>
          
          <Link
            to="/attendance"
            className="flex items-center p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors duration-200"
          >
            <span className="text-2xl mr-3">📝</span>
            <div>
              <h3 className="font-medium text-gray-900">Mark Attendance</h3>
              <p className="text-sm text-gray-600">Record daily attendance</p>
            </div>
          </Link>
          
          <Link
            to="/leave-requests"
            className="flex items-center p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors duration-200"
          >
            <span className="text-2xl mr-3">📋</span>
            <div>
              <h3 className="font-medium text-gray-900">Leave Request</h3>
              <p className="text-sm text-gray-600">Manage leave applications</p>
            </div>
          </Link>
          
          <Link
            to="/payroll"
            className="flex items-center p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors duration-200"
          >
            <span className="text-2xl mr-3">💰</span>
            <div>
              <h3 className="font-medium text-gray-900">Process Payroll</h3>
              <p className="text-sm text-gray-600">Handle salary payments</p>
            </div>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;