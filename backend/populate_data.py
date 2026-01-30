import os
import django
from datetime import date, timedelta
from decimal import Decimal

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hrms_project.settings')
django.setup()

from hrms.models import Employee, Department, Attendance, LeaveType, LeaveRequest, Performance, Payroll

def populate_data():
    print("Creating sample data...")
    
    # Create Departments
    departments = [
        {'name': 'Engineering', 'description': 'Software Development Team', 'budget': Decimal('500000.00')},
        {'name': 'Marketing', 'description': 'Marketing and Sales Team', 'budget': Decimal('200000.00')},
        {'name': 'HR', 'description': 'Human Resources Team', 'budget': Decimal('150000.00')},
        {'name': 'Finance', 'description': 'Finance and Accounting Team', 'budget': Decimal('180000.00')},
    ]
    
    for dept_data in departments:
        dept, created = Department.objects.get_or_create(name=dept_data['name'], defaults=dept_data)
        if created:
            print(f"Created department: {dept.name}")
    
    # Create Leave Types
    leave_types = [
        {'name': 'Annual Leave', 'days_allowed': 21, 'description': 'Yearly vacation days', 'is_paid': True},
        {'name': 'Sick Leave', 'days_allowed': 10, 'description': 'Medical leave', 'is_paid': True},
        {'name': 'Personal Leave', 'days_allowed': 5, 'description': 'Personal time off', 'is_paid': False},
        {'name': 'Maternity Leave', 'days_allowed': 90, 'description': 'Maternity leave', 'is_paid': True},
    ]
    
    for leave_data in leave_types:
        leave_type, created = LeaveType.objects.get_or_create(name=leave_data['name'], defaults=leave_data)
        if created:
            print(f"Created leave type: {leave_type.name}")
    
    # Create Sample Employees
    employees = [
        {
            'employee_id': 'EMP001',
            'full_name': 'John Smith',
            'email': 'john.smith@company.com',
            'phone': '+1-555-0101',
            'department': 'Engineering',
            'position': 'Senior Software Engineer',
            'hire_date': date(2022, 1, 15),
            'salary': Decimal('85000.00'),
            'status': 'Active'
        },
        {
            'employee_id': 'EMP002',
            'full_name': 'Sarah Johnson',
            'email': 'sarah.johnson@company.com',
            'phone': '+1-555-0102',
            'department': 'Marketing',
            'position': 'Marketing Manager',
            'hire_date': date(2021, 6, 10),
            'salary': Decimal('75000.00'),
            'status': 'Active'
        },
        {
            'employee_id': 'EMP003',
            'full_name': 'Mike Davis',
            'email': 'mike.davis@company.com',
            'phone': '+1-555-0103',
            'department': 'Engineering',
            'position': 'Frontend Developer',
            'hire_date': date(2023, 3, 20),
            'salary': Decimal('70000.00'),
            'status': 'Active'
        },
        {
            'employee_id': 'EMP004',
            'full_name': 'Emily Brown',
            'email': 'emily.brown@company.com',
            'phone': '+1-555-0104',
            'department': 'HR',
            'position': 'HR Specialist',
            'hire_date': date(2022, 8, 5),
            'salary': Decimal('60000.00'),
            'status': 'Active'
        },
        {
            'employee_id': 'EMP005',
            'full_name': 'David Wilson',
            'email': 'david.wilson@company.com',
            'phone': '+1-555-0105',
            'department': 'Finance',
            'position': 'Financial Analyst',
            'hire_date': date(2021, 11, 12),
            'salary': Decimal('65000.00'),
            'status': 'Active'
        }
    ]
    
    for emp_data in employees:
        emp, created = Employee.objects.get_or_create(employee_id=emp_data['employee_id'], defaults=emp_data)
        if created:
            print(f"Created employee: {emp.full_name}")
    
    # Create Sample Attendance Records (last 30 days)
    employees_list = Employee.objects.all()
    today = date.today()
    
    for i in range(30):
        current_date = today - timedelta(days=i)
        # Skip weekends
        if current_date.weekday() < 5:  # Monday = 0, Sunday = 6
            for employee in employees_list:
                # 90% chance of being present
                import random
                if random.random() < 0.9:
                    status = 'Present'
                    if random.random() < 0.1:  # 10% chance of being late
                        status = 'Late'
                else:
                    status = 'Absent'
                
                attendance, created = Attendance.objects.get_or_create(
                    employee=employee,
                    date=current_date,
                    defaults={
                        'status': status,
                        'check_in_time': '09:00:00' if status != 'Absent' else None,
                        'check_out_time': '17:30:00' if status == 'Present' else None,
                        'hours_worked': 8.5 if status == 'Present' else (4.0 if status == 'Half Day' else 0)
                    }
                )
    
    print("Sample attendance records created for the last 30 days")
    
    # Create Sample Leave Requests
    annual_leave = LeaveType.objects.get(name='Annual Leave')
    sick_leave = LeaveType.objects.get(name='Sick Leave')
    
    leave_requests = [
        {
            'employee': employees_list[0],
            'leave_type': annual_leave,
            'start_date': date(2026, 2, 10),
            'end_date': date(2026, 2, 14),
            'days_requested': 5,
            'reason': 'Family vacation',
            'status': 'Pending'
        },
        {
            'employee': employees_list[1],
            'leave_type': sick_leave,
            'start_date': date(2026, 1, 25),
            'end_date': date(2026, 1, 26),
            'days_requested': 2,
            'reason': 'Medical appointment',
            'status': 'Approved',
            'approved_by': 'ADMIN'
        }
    ]
    
    for req_data in leave_requests:
        req, created = LeaveRequest.objects.get_or_create(
            employee=req_data['employee'],
            start_date=req_data['start_date'],
            defaults=req_data
        )
        if created:
            print(f"Created leave request for {req.employee.full_name}")
    
    print("Sample data population completed!")

if __name__ == '__main__':
    populate_data()