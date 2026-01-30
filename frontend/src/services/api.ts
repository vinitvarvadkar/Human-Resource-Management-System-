import axios from 'axios';
import { 
  Employee, EmployeeCreate, Department, AttendanceRecord, AttendanceCreate, AttendanceStats,
  LeaveType, LeaveRequest, LeaveRequestCreate, Performance, PerformanceCreate,
  Payroll, PayrollCreate, Notification, DashboardStats, DepartmentStats
} from '../types';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Employee API
export const employeeApi = {
  getAll: (params?: { search?: string; department?: string; status?: string }): Promise<Employee[]> => 
    api.get('/api/employees/', { params }).then(response => response.data),
  
  getById: (employeeId: string): Promise<Employee> =>
    api.get(`/api/employees/${employeeId}/`).then(response => response.data),
  
  create: (employee: EmployeeCreate): Promise<Employee> =>
    api.post('/api/employees/', employee).then(response => response.data),
  
  update: (employeeId: string, employee: Partial<EmployeeCreate>): Promise<Employee> =>
    api.put(`/api/employees/${employeeId}/`, employee).then(response => response.data),
  
  delete: (employeeId: string): Promise<void> =>
    api.delete(`/api/employees/${employeeId}/`).then(response => response.data),
  
  bulkImport: (employees: EmployeeCreate[]): Promise<any> =>
    api.post('/api/employees/bulk-import/', { employees }).then(response => response.data),
  
  exportCSV: (): Promise<Blob> =>
    api.get('/api/export/employees/', { responseType: 'blob' }).then(response => response.data),
};

// Department API
export const departmentApi = {
  getAll: (): Promise<Department[]> =>
    api.get('/api/departments/').then(response => response.data),
  
  create: (department: Partial<Department>): Promise<Department> =>
    api.post('/api/departments/', department).then(response => response.data),
  
  update: (id: number, department: Partial<Department>): Promise<Department> =>
    api.put(`/api/departments/${id}/`, department).then(response => response.data),
  
  delete: (id: number): Promise<void> =>
    api.delete(`/api/departments/${id}/`).then(response => response.data),
};

// Attendance API
export const attendanceApi = {
  getAll: (params?: { 
    employee_id?: string; 
    start_date?: string; 
    end_date?: string; 
    status?: string; 
  }): Promise<AttendanceRecord[]> => {
    return api.get('/api/attendance/', { params }).then(response => response.data);
  },
  
  mark: (attendance: AttendanceCreate): Promise<AttendanceRecord> =>
    api.post('/api/attendance/', attendance).then(response => response.data),
  
  getStats: (employeeId: string): Promise<AttendanceStats> =>
    api.get(`/api/attendance/stats/${employeeId}/`).then(response => response.data),
  
  exportCSV: (): Promise<Blob> =>
    api.get('/api/export/attendance/', { responseType: 'blob' }).then(response => response.data),
};

// Leave Management API
export const leaveApi = {
  getTypes: (): Promise<LeaveType[]> =>
    api.get('/api/leave-types/').then(response => response.data),
  
  createType: (leaveType: Partial<LeaveType>): Promise<LeaveType> =>
    api.post('/api/leave-types/', leaveType).then(response => response.data),
  
  getRequests: (params?: { employee_id?: string; status?: string }): Promise<LeaveRequest[]> =>
    api.get('/api/leave-requests/', { params }).then(response => response.data),
  
  createRequest: (request: LeaveRequestCreate): Promise<LeaveRequest> =>
    api.post('/api/leave-requests/', request).then(response => response.data),
  
  updateRequest: (id: number, request: Partial<LeaveRequest>): Promise<LeaveRequest> =>
    api.put(`/api/leave-requests/${id}/`, request).then(response => response.data),
  
  deleteRequest: (id: number): Promise<void> =>
    api.delete(`/api/leave-requests/${id}/`).then(response => response.data),
};

// Performance API
export const performanceApi = {
  getAll: (params?: { employee_id?: string }): Promise<Performance[]> =>
    api.get('/api/performance/', { params }).then(response => response.data),
  
  create: (performance: PerformanceCreate): Promise<Performance> =>
    api.post('/api/performance/', performance).then(response => response.data),
};

// Payroll API
export const payrollApi = {
  getAll: (params?: { employee_id?: string; status?: string }): Promise<Payroll[]> =>
    api.get('/api/payroll/', { params }).then(response => response.data),
  
  create: (payroll: PayrollCreate): Promise<Payroll> =>
    api.post('/api/payroll/', payroll).then(response => response.data),
};

// Notification API
export const notificationApi = {
  getAll: (params?: { employee_id?: string }): Promise<Notification[]> =>
    api.get('/api/notifications/', { params }).then(response => response.data),
};

// Dashboard API
export const dashboardApi = {
  getStats: (): Promise<DashboardStats> =>
    api.get('/api/dashboard/stats/').then(response => response.data),
  
  getDepartmentStats: (): Promise<DepartmentStats[]> =>
    api.get('/api/analytics/department-stats/').then(response => response.data),
};

export default api;