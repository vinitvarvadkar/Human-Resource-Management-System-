export interface Employee {
  id: number;
  employee_id: string;
  full_name: string;
  email: string;
  phone?: string;
  department: string;
  position?: string;
  hire_date?: string;
  salary?: number;
  manager_id?: string;
  status: 'Active' | 'Inactive' | 'Terminated';
  address?: string;
  emergency_contact?: string;
  emergency_phone?: string;
  profile_picture?: string;
  created_at: string;
  updated_at: string;
}

export interface EmployeeCreate {
  employee_id: string;
  full_name: string;
  email: string;
  phone?: string;
  department: string;
  position?: string;
  hire_date?: string;
  salary?: number;
  manager_id?: string;
  address?: string;
  emergency_contact?: string;
  emergency_phone?: string;
}

export interface Department {
  id: number;
  name: string;
  description?: string;
  manager_id?: string;
  budget?: number;
  employee_count: number;
  created_at: string;
}

export interface AttendanceRecord {
  id: number;
  employee_id: string;
  date: string;
  status: 'Present' | 'Absent' | 'Late' | 'Half Day';
  check_in_time?: string;
  check_out_time?: string;
  hours_worked?: number;
  notes?: string;
  employee_name?: string;
}

export interface AttendanceCreate {
  employee_id: string;
  date: string;
  status: 'Present' | 'Absent' | 'Late' | 'Half Day';
  check_in_time?: string;
  check_out_time?: string;
  hours_worked?: number;
  notes?: string;
}

export interface AttendanceStats {
  employee_id: string;
  employee_name: string;
  total_days: number;
  present_days: number;
  absent_days: number;
  late_days: number;
  half_days: number;
  attendance_percentage: number;
}

export interface LeaveType {
  id: number;
  name: string;
  days_allowed: number;
  description?: string;
  is_paid: boolean;
}

export interface LeaveRequest {
  id: number;
  employee_id: string;
  employee_name: string;
  leave_type: number;
  leave_type_name: string;
  start_date: string;
  end_date: string;
  days_requested: number;
  reason: string;
  status: 'Pending' | 'Approved' | 'Rejected' | 'Cancelled';
  approved_by?: string;
  approved_date?: string;
  comments?: string;
  created_at: string;
}

export interface LeaveRequestCreate {
  employee_id: string;
  leave_type: number;
  start_date: string;
  end_date: string;
  days_requested: number;
  reason: string;
}

export interface Performance {
  id: number;
  employee_id: string;
  employee_name: string;
  review_period_start: string;
  review_period_end: string;
  overall_rating: number;
  goals_achievement: number;
  communication: number;
  teamwork: number;
  technical_skills: number;
  average_rating: number;
  comments?: string;
  reviewer_id: string;
  created_at: string;
}

export interface PerformanceCreate {
  employee_id: string;
  review_period_start: string;
  review_period_end: string;
  overall_rating: number;
  goals_achievement: number;
  communication: number;
  teamwork: number;
  technical_skills: number;
  comments?: string;
  reviewer_id: string;
}

export interface Payroll {
  id: number;
  employee_id: string;
  employee_name: string;
  pay_period_start: string;
  pay_period_end: string;
  basic_salary: number;
  overtime_hours: number;
  overtime_rate: number;
  bonuses: number;
  deductions: number;
  tax_deduction: number;
  net_salary: number;
  status: 'Draft' | 'Processed' | 'Paid';
  created_at: string;
}

export interface PayrollCreate {
  employee_id: string;
  pay_period_start: string;
  pay_period_end: string;
  basic_salary: number;
  overtime_hours?: number;
  overtime_rate?: number;
  bonuses?: number;
  deductions?: number;
  tax_deduction?: number;
}

export interface Notification {
  id: number;
  employee: string;
  employee_name: string;
  title: string;
  message: string;
  notification_type: 'leave_request' | 'attendance_alert' | 'performance_review' | 'payroll' | 'general';
  is_read: boolean;
  created_at: string;
}

export interface DashboardStats {
  total_employees: number;
  active_employees: number;
  present_today: number;
  absent_today: number;
  pending_leave_requests: number;
  departments_count: number;
  average_attendance_rate: number;
  total_payroll_this_month: number;
}

export interface DepartmentStats {
  department: string;
  total_employees: number;
  present_today: number;
  absent_today: number;
  attendance_rate: number;
  average_salary: number;
}