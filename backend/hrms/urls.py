from django.urls import path
from . import views

urlpatterns = [
    # Employee URLs
    path('employees/', views.EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<str:employee_id>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    
    # Department URLs
    path('departments/', views.DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department-detail'),
    
    # Attendance URLs
    path('attendance/', views.AttendanceListCreateView.as_view(), name='attendance-list-create'),
    path('attendance/stats/<str:employee_id>/', views.attendance_stats, name='attendance-stats'),
    
    # Leave Management URLs
    path('leave-types/', views.LeaveTypeListCreateView.as_view(), name='leave-type-list-create'),
    path('leave-requests/', views.LeaveRequestListCreateView.as_view(), name='leave-request-list-create'),
    path('leave-requests/<int:pk>/', views.LeaveRequestDetailView.as_view(), name='leave-request-detail'),
    
    # Performance URLs
    path('performance/', views.PerformanceListCreateView.as_view(), name='performance-list-create'),
    
    # Payroll URLs
    path('payroll/', views.PayrollListCreateView.as_view(), name='payroll-list-create'),
    
    # Notification URLs
    path('notifications/', views.NotificationListView.as_view(), name='notification-list'),
    
    # Dashboard and Analytics URLs
    path('dashboard/stats/', views.dashboard_stats, name='dashboard-stats'),
    path('analytics/department-stats/', views.department_stats, name='department-stats'),
    
    # Bulk Operations URLs
    path('employees/bulk-import/', views.bulk_import_employees, name='bulk-import-employees'),
    path('export/employees/', views.export_employees_csv, name='export-employees'),
    path('export/attendance/', views.export_attendance_csv, name='export-attendance'),
]