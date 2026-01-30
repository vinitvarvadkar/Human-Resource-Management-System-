from rest_framework import serializers
from .models import Employee, Attendance, LeaveRequest, LeaveType, Performance, Payroll, Department, Notification
import re
from datetime import date, datetime

class DepartmentSerializer(serializers.ModelSerializer):
    employee_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'manager_id', 'budget', 'employee_count', 'created_at']
    
    def get_employee_count(self, obj):
        return Employee.objects.filter(department=obj.name, status='Active').count()

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id', 'employee_id', 'full_name', 'email', 'phone', 'department', 
            'position', 'hire_date', 'salary', 'manager_id', 'status', 'address',
            'emergency_contact', 'emergency_phone', 'profile_picture', 'created_at', 'updated_at'
        ]

    def validate_employee_id(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError('Employee ID cannot be empty')
        
        if not re.match(r'^[A-Za-z0-9_-]+$', value):
            raise serializers.ValidationError('Employee ID can only contain letters, numbers, hyphens, and underscores')
        
        return value.strip()

    def validate_full_name(self, value):
        if not value or len(value.strip()) < 2:
            raise serializers.ValidationError('Full name must be at least 2 characters long')
        
        return value.strip()

    def validate_department(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError('Department cannot be empty')
        
        return value.strip()

class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id', 'full_name', 'email', 'phone', 'department', 'position', 'hire_date', 'salary', 'manager_id', 'address', 'emergency_contact', 'emergency_phone']

class AttendanceSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    employee_id = serializers.CharField(write_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'employee_id', 'date', 'status', 'check_in_time', 'check_out_time', 'hours_worked', 'notes', 'employee_name']

    def validate_status(self, value):
        if value not in ['Present', 'Absent', 'Late', 'Half Day']:
            raise serializers.ValidationError('Status must be Present, Absent, Late, or Half Day')
        return value

    def create(self, validated_data):
        employee_id = validated_data.pop('employee_id')
        try:
            employee = Employee.objects.get(employee_id=employee_id)
        except Employee.DoesNotExist:
            raise serializers.ValidationError({'employee_id': 'Employee not found'})
        
        validated_data['employee'] = employee
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['employee_id'] = instance.employee.employee_id
        return representation

class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = ['id', 'name', 'days_allowed', 'description', 'is_paid']

class LeaveRequestSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    employee_id = serializers.CharField(write_only=True)
    leave_type_name = serializers.CharField(source='leave_type.name', read_only=True)

    class Meta:
        model = LeaveRequest
        fields = [
            'id', 'employee_id', 'employee_name', 'leave_type', 'leave_type_name',
            'start_date', 'end_date', 'days_requested', 'reason', 'status',
            'approved_by', 'approved_date', 'comments', 'created_at'
        ]

    def create(self, validated_data):
        employee_id = validated_data.pop('employee_id')
        try:
            employee = Employee.objects.get(employee_id=employee_id)
        except Employee.DoesNotExist:
            raise serializers.ValidationError({'employee_id': 'Employee not found'})
        
        validated_data['employee'] = employee
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['employee_id'] = instance.employee.employee_id
        return representation

class PerformanceSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    employee_id = serializers.CharField(write_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Performance
        fields = [
            'id', 'employee_id', 'employee_name', 'review_period_start', 'review_period_end',
            'overall_rating', 'goals_achievement', 'communication', 'teamwork', 'technical_skills',
            'average_rating', 'comments', 'reviewer_id', 'created_at'
        ]

    def get_average_rating(self, obj):
        ratings = [obj.overall_rating, obj.goals_achievement, obj.communication, obj.teamwork, obj.technical_skills]
        return round(sum(ratings) / len(ratings), 2)

    def create(self, validated_data):
        employee_id = validated_data.pop('employee_id')
        try:
            employee = Employee.objects.get(employee_id=employee_id)
        except Employee.DoesNotExist:
            raise serializers.ValidationError({'employee_id': 'Employee not found'})
        
        validated_data['employee'] = employee
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['employee_id'] = instance.employee.employee_id
        return representation

class PayrollSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    employee_id = serializers.CharField(write_only=True)

    class Meta:
        model = Payroll
        fields = [
            'id', 'employee_id', 'employee_name', 'pay_period_start', 'pay_period_end',
            'basic_salary', 'overtime_hours', 'overtime_rate', 'bonuses', 'deductions',
            'tax_deduction', 'net_salary', 'status', 'created_at'
        ]

    def create(self, validated_data):
        employee_id = validated_data.pop('employee_id')
        try:
            employee = Employee.objects.get(employee_id=employee_id)
        except Employee.DoesNotExist:
            raise serializers.ValidationError({'employee_id': 'Employee not found'})
        
        validated_data['employee'] = employee
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['employee_id'] = instance.employee.employee_id
        return representation

class NotificationSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'employee', 'employee_name', 'title', 'message', 'notification_type', 'is_read', 'created_at']

class DashboardStatsSerializer(serializers.Serializer):
    total_employees = serializers.IntegerField()
    active_employees = serializers.IntegerField()
    present_today = serializers.IntegerField()
    absent_today = serializers.IntegerField()
    pending_leave_requests = serializers.IntegerField()
    departments_count = serializers.IntegerField()
    average_attendance_rate = serializers.FloatField()
    total_payroll_this_month = serializers.DecimalField(max_digits=12, decimal_places=2)

class AttendanceStatsSerializer(serializers.Serializer):
    employee_id = serializers.CharField()
    employee_name = serializers.CharField()
    total_days = serializers.IntegerField()
    present_days = serializers.IntegerField()
    absent_days = serializers.IntegerField()
    late_days = serializers.IntegerField()
    half_days = serializers.IntegerField()
    attendance_percentage = serializers.FloatField()

class DepartmentStatsSerializer(serializers.Serializer):
    department = serializers.CharField()
    total_employees = serializers.IntegerField()
    present_today = serializers.IntegerField()
    absent_today = serializers.IntegerField()
    attendance_rate = serializers.FloatField()
    average_salary = serializers.DecimalField(max_digits=10, decimal_places=2)