from rest_framework import generics, status, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from django.db.models import Count, Q, Avg, Sum
from django.utils import timezone
from datetime import date, datetime, timedelta
from decimal import Decimal
import csv
from django.http import HttpResponse
from .models import Employee, Attendance, LeaveRequest, LeaveType, Performance, Payroll, Department, Notification
from .serializers import (
    EmployeeSerializer, EmployeeCreateSerializer, AttendanceSerializer, 
    LeaveRequestSerializer, LeaveTypeSerializer, PerformanceSerializer, 
    PayrollSerializer, DepartmentSerializer, NotificationSerializer,
    DashboardStatsSerializer, AttendanceStatsSerializer, DepartmentStatsSerializer
)

# Employee Views
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['employee_id', 'full_name', 'email', 'department']
    ordering_fields = ['employee_id', 'full_name', 'hire_date', 'department']
    ordering = ['employee_id']

    def get_queryset(self):
        queryset = Employee.objects.all()
        department = self.request.query_params.get('department', None)
        status_filter = self.request.query_params.get('status', None)
        
        if department:
            queryset = queryset.filter(department=department)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
            
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EmployeeCreateSerializer
        return EmployeeSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            if 'employee_id' in str(e):
                return Response(
                    {'detail': 'Employee ID already exists'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            elif 'email' in str(e):
                return Response(
                    {'detail': 'Email already exists'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                return Response(
                    {'detail': 'Database error occurred'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'employee_id'

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({'message': 'Employee deleted successfully'})
        except Employee.DoesNotExist:
            return Response(
                {'detail': 'Employee not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

# Department Views
class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# Attendance Views
class AttendanceListCreateView(generics.ListCreateAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        queryset = Attendance.objects.select_related('employee').all()
        employee_id = self.request.query_params.get('employee_id', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        status_filter = self.request.query_params.get('status', None)
        
        if employee_id:
            queryset = queryset.filter(employee__employee_id=employee_id)
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
            
        return queryset.order_by('-date')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        employee_id = request.data.get('employee_id')
        date_val = request.data.get('date')
        
        try:
            employee = Employee.objects.get(employee_id=employee_id)
        except Employee.DoesNotExist:
            return Response(
                {'detail': 'Employee not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Check if attendance already exists for this date
        existing_attendance = Attendance.objects.filter(
            employee=employee, 
            date=date_val
        ).first()
        
        if existing_attendance:
            # Update existing attendance
            for attr, value in serializer.validated_data.items():
                if attr != 'employee':
                    setattr(existing_attendance, attr, value)
            existing_attendance.save()
            serializer = AttendanceSerializer(existing_attendance)
            return Response(serializer.data)
        else:
            # Create new attendance
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# Leave Management Views
class LeaveTypeListCreateView(generics.ListCreateAPIView):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer

class LeaveRequestListCreateView(generics.ListCreateAPIView):
    serializer_class = LeaveRequestSerializer

    def get_queryset(self):
        queryset = LeaveRequest.objects.select_related('employee', 'leave_type').all()
        employee_id = self.request.query_params.get('employee_id', None)
        status_filter = self.request.query_params.get('status', None)
        
        if employee_id:
            queryset = queryset.filter(employee__employee_id=employee_id)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
            
        return queryset.order_by('-created_at')

class LeaveRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer

# Performance Views
class PerformanceListCreateView(generics.ListCreateAPIView):
    serializer_class = PerformanceSerializer

    def get_queryset(self):
        queryset = Performance.objects.select_related('employee').all()
        employee_id = self.request.query_params.get('employee_id', None)
        
        if employee_id:
            queryset = queryset.filter(employee__employee_id=employee_id)
            
        return queryset.order_by('-created_at')

# Payroll Views
class PayrollListCreateView(generics.ListCreateAPIView):
    serializer_class = PayrollSerializer

    def get_queryset(self):
        queryset = Payroll.objects.select_related('employee').all()
        employee_id = self.request.query_params.get('employee_id', None)
        status_filter = self.request.query_params.get('status', None)
        
        if employee_id:
            queryset = queryset.filter(employee__employee_id=employee_id)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
            
        return queryset.order_by('-created_at')

# Notification Views
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        employee_id = self.request.query_params.get('employee_id', None)
        if employee_id:
            return Notification.objects.filter(employee__employee_id=employee_id)
        return Notification.objects.all()

# Dashboard and Analytics Views
@api_view(['GET'])
def dashboard_stats(request):
    today = date.today()
    
    # Basic counts
    total_employees = Employee.objects.count()
    active_employees = Employee.objects.filter(status='Active').count()
    
    # Today's attendance
    today_attendance = Attendance.objects.filter(date=today)
    present_today = today_attendance.filter(status__in=['Present', 'Late', 'Half Day']).count()
    absent_today = today_attendance.filter(status='Absent').count()
    
    # Leave requests
    pending_leave_requests = LeaveRequest.objects.filter(status='Pending').count()
    
    # Departments
    departments_count = Department.objects.count()
    
    # Attendance rate (last 30 days)
    thirty_days_ago = today - timedelta(days=30)
    total_attendance_records = Attendance.objects.filter(date__gte=thirty_days_ago).count()
    present_records = Attendance.objects.filter(
        date__gte=thirty_days_ago, 
        status__in=['Present', 'Late', 'Half Day']
    ).count()
    average_attendance_rate = (present_records / total_attendance_records * 100) if total_attendance_records > 0 else 0
    
    # Payroll this month
    current_month_start = today.replace(day=1)
    total_payroll_this_month = Payroll.objects.filter(
        pay_period_start__gte=current_month_start,
        status='Processed'
    ).aggregate(total=Sum('net_salary'))['total'] or Decimal('0.00')
    
    stats = {
        'total_employees': total_employees,
        'active_employees': active_employees,
        'present_today': present_today,
        'absent_today': absent_today,
        'pending_leave_requests': pending_leave_requests,
        'departments_count': departments_count,
        'average_attendance_rate': round(average_attendance_rate, 2),
        'total_payroll_this_month': total_payroll_this_month
    }
    
    serializer = DashboardStatsSerializer(stats)
    return Response(serializer.data)

@api_view(['GET'])
def attendance_stats(request, employee_id):
    try:
        employee = Employee.objects.get(employee_id=employee_id)
    except Employee.DoesNotExist:
        return Response(
            {'detail': 'Employee not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    attendance_records = Attendance.objects.filter(employee=employee)
    total_records = attendance_records.count()
    present_days = attendance_records.filter(status='Present').count()
    absent_days = attendance_records.filter(status='Absent').count()
    late_days = attendance_records.filter(status='Late').count()
    half_days = attendance_records.filter(status='Half Day').count()
    
    attendance_percentage = round((present_days / total_records * 100) if total_records > 0 else 0, 2)
    
    stats = {
        'employee_id': employee_id,
        'employee_name': employee.full_name,
        'total_days': total_records,
        'present_days': present_days,
        'absent_days': absent_days,
        'late_days': late_days,
        'half_days': half_days,
        'attendance_percentage': attendance_percentage
    }
    
    serializer = AttendanceStatsSerializer(stats)
    return Response(serializer.data)

@api_view(['GET'])
def department_stats(request):
    departments = Department.objects.all()
    today = date.today()
    stats = []
    
    for dept in departments:
        dept_employees = Employee.objects.filter(department=dept.name, status='Active')
        total_employees = dept_employees.count()
        
        if total_employees > 0:
            # Today's attendance for this department
            today_attendance = Attendance.objects.filter(
                employee__in=dept_employees,
                date=today
            )
            present_today = today_attendance.filter(status__in=['Present', 'Late', 'Half Day']).count()
            absent_today = today_attendance.filter(status='Absent').count()
            attendance_rate = (present_today / total_employees * 100) if total_employees > 0 else 0
            
            # Average salary
            avg_salary = dept_employees.filter(salary__isnull=False).aggregate(
                avg=Avg('salary')
            )['avg'] or Decimal('0.00')
            
            stats.append({
                'department': dept.name,
                'total_employees': total_employees,
                'present_today': present_today,
                'absent_today': absent_today,
                'attendance_rate': round(attendance_rate, 2),
                'average_salary': avg_salary
            })
    
    serializer = DepartmentStatsSerializer(stats, many=True)
    return Response(serializer.data)

# Bulk Operations
@api_view(['POST'])
def bulk_import_employees(request):
    employees_data = request.data.get('employees', [])
    created_count = 0
    errors = []
    
    for emp_data in employees_data:
        try:
            serializer = EmployeeCreateSerializer(data=emp_data)
            if serializer.is_valid():
                serializer.save()
                created_count += 1
            else:
                errors.append({
                    'employee_id': emp_data.get('employee_id', 'Unknown'),
                    'errors': serializer.errors
                })
        except Exception as e:
            errors.append({
                'employee_id': emp_data.get('employee_id', 'Unknown'),
                'errors': str(e)
            })
    
    return Response({
        'created_count': created_count,
        'total_count': len(employees_data),
        'errors': errors
    })

@api_view(['GET'])
def export_employees_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'
    
    writer = csv.writer(response)
    writer.writerow([
        'Employee ID', 'Full Name', 'Email', 'Phone', 'Department', 
        'Position', 'Hire Date', 'Salary', 'Status'
    ])
    
    employees = Employee.objects.all()
    for emp in employees:
        writer.writerow([
            emp.employee_id, emp.full_name, emp.email, emp.phone or '',
            emp.department, emp.position or '', emp.hire_date or '',
            emp.salary or '', emp.status
        ])
    
    return response

@api_view(['GET'])
def export_attendance_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance.csv"'
    
    writer = csv.writer(response)
    writer.writerow([
        'Employee ID', 'Employee Name', 'Date', 'Status', 
        'Check In', 'Check Out', 'Hours Worked'
    ])
    
    attendance_records = Attendance.objects.select_related('employee').all()
    for record in attendance_records:
        writer.writerow([
            record.employee.employee_id, record.employee.full_name,
            record.date, record.status, record.check_in_time or '',
            record.check_out_time or '', record.hours_worked or ''
        ])
    
    return response

@api_view(['GET'])
def root_view(request):
    return Response({'message': 'HRMS Lite API is running'})