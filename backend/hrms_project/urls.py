"""
URL configuration for hrms_project project.
"""
from django.contrib import admin
from django.urls import path, include
from hrms.views import root_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_view, name='root'),
    path('api/', include('hrms.urls')),
]
