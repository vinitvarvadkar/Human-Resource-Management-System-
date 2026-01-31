# 🚀 HRMS Lite Pro - Advanced Human Resource Management System

A comprehensive, hackathon-level Human Resource Management System built with modern technologies. This full-stack application provides enterprise-grade HR functionality with a beautiful, responsive interface.

## 🌟 Live Demo

- **Frontend:** http://localhost:3001
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/admin

## ✨ Advanced Features

### 🎯 Core HR Management
- **Employee Management** - Complete CRUD operations with advanced filtering
- **Attendance Tracking** - Real-time attendance with multiple status types
- **Leave Management** - Comprehensive leave request system with approval workflow
- **Performance Reviews** - Employee performance tracking and analytics
- **Payroll Management** - Salary processing with overtime and deductions

### 📊 Analytics & Reporting
- **Real-time Dashboard** - Live statistics and KPIs
- **Department Analytics** - Performance metrics by department
- **Attendance Reports** - Detailed attendance analytics with charts
- **Export Functionality** - CSV export for all data types
- **Advanced Filtering** - Multi-parameter search and filtering

### 🔧 Advanced Operations
- **Bulk Import/Export** - Mass employee data operations
- **Notification System** - Real-time alerts and notifications
- **Multi-status Tracking** - Present, Absent, Late, Half Day statuses
- **Salary Calculations** - Automated payroll with tax deductions
- **Leave Balance Tracking** - Automatic leave balance management

### 🎨 Professional UI/UX
- **Modern Design** - Clean, professional interface with Tailwind CSS
- **Responsive Layout** - Mobile-first design that works on all devices
- **Interactive Charts** - Visual data representation
- **Loading States** - Smooth user experience with proper feedback
- **Error Handling** - Comprehensive error management

## 🛠️ Tech Stack

### Frontend
- **React 18** with TypeScript for type safety
- **Tailwind CSS** for modern, responsive styling
- **React Router** for client-side routing
- **React Hook Form** for efficient form handling
- **Axios** for API communication

### Backend
- **Django 4.2** with Python for robust backend
- **Django REST Framework** for powerful API development
- **SQLite** database for easy deployment
- **Django CORS Headers** for cross-origin requests
- **Comprehensive validation** and error handling

### Development Tools
- **TypeScript** for enhanced development experience
- **ESLint** for code quality
- **Hot Reload** for rapid development
- **Modular Architecture** for maintainability

## 📁 Project Structure

```
hrms-lite-pro/
├── frontend/                  # React TypeScript Application
│   ├── src/
│   │   ├── components/        # Reusable UI components
│   │   │   ├── Layout.tsx     # Main layout wrapper
│   │   │   ├── LoadingSpinner.tsx
│   │   │   └── ErrorMessage.tsx
│   │   ├── pages/             # Main application pages
│   │   │   ├── Dashboard.tsx  # Analytics dashboard
│   │   │   ├── Employees.tsx  # Employee management
│   │   │   ├── Attendance.tsx # Attendance tracking
│   │   │   └── LeaveManagement.tsx # Leave requests
│   │   ├── services/          # API service layer
│   │   │   └── api.ts         # Centralized API calls
│   │   ├── types/             # TypeScript definitions
│   │   │   └── index.ts       # All type definitions
│   │   └── App.tsx            # Main app component
│   ├── public/
│   └── package.json
├── backend/                   # Django Application
│   ├── hrms_project/          # Django project settings
│   │   ├── settings.py        # Configuration
│   │   └── urls.py            # URL routing
│   ├── hrms/                  # Main Django app
│   │   ├── models.py          # Database models
│   │   ├── serializers.py     # API serializers
│   │   ├── views.py           # API views
│   │   └── urls.py            # App URLs
│   ├── requirements.txt       # Python dependencies
│   ├── manage.py              # Django management
│   └── populate_data.py       # Sample data script
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- **Node.js 16+** and npm
- **Python 3.8+**
- Git

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd hrms-lite-pro
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create sample data (optional)
python populate_data.py

# Start the Django server
python manage.py runserver 0.0.0.0:8000
```

### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start the development server
PORT=3001 npm start
```

### 4. Access the Application
- **Frontend:** http://localhost:3001
- **Backend API:** http://localhost:8000
- **Django Admin:** http://localhost:8000/admin

## 📋 API Endpoints

### Employee Management
- `GET /api/employees/` - List all employees with filtering
- `POST /api/employees/` - Create new employee
- `GET /api/employees/{id}/` - Get employee details
- `PUT /api/employees/{id}/` - Update employee
- `DELETE /api/employees/{id}/` - Delete employee
- `POST /api/employees/bulk-import/` - Bulk import employees

### Attendance Management
- `GET /api/attendance/` - Get attendance records with filtering
- `POST /api/attendance/` - Mark attendance
- `GET /api/attendance/stats/{employee_id}/` - Get attendance statistics

### Leave Management
- `GET /api/leave-types/` - Get all leave types
- `POST /api/leave-types/` - Create leave type
- `GET /api/leave-requests/` - Get leave requests with filtering
- `POST /api/leave-requests/` - Create leave request
- `PUT /api/leave-requests/{id}/` - Update leave request status

### Performance Management
- `GET /api/performance/` - Get performance reviews
- `POST /api/performance/` - Create performance review

### Payroll Management
- `GET /api/payroll/` - Get payroll records
- `POST /api/payroll/` - Process payroll

### Analytics & Reports
- `GET /api/dashboard/stats/` - Get dashboard statistics
- `GET /api/analytics/department-stats/` - Get department analytics
- `GET /api/export/employees/` - Export employees to CSV
- `GET /api/export/attendance/` - Export attendance to CSV

## 🎯 Key Features Demonstrated

### 1. Full-Stack Development
- **Frontend:** Modern React with TypeScript
- **Backend:** Robust Django REST API
- **Database:** Proper relational database design
- **Integration:** Seamless frontend-backend communication

### 2. Advanced UI/UX
- **Responsive Design:** Works on desktop, tablet, and mobile
- **Interactive Dashboard:** Real-time statistics and charts
- **Professional Styling:** Clean, modern interface
- **User Experience:** Loading states, error handling, form validation

### 3. Enterprise Features
- **Role-based Operations:** Different user capabilities
- **Data Export/Import:** CSV functionality for data management
- **Advanced Filtering:** Multi-parameter search capabilities
- **Bulk Operations:** Mass data processing
- **Audit Trail:** Track changes and updates

### 4. Performance & Scalability
- **Optimized Queries:** Efficient database operations
- **Lazy Loading:** Improved performance with pagination
- **Caching Strategy:** Reduced API calls
- **Error Boundaries:** Graceful error handling

## 🏆 Hackathon-Level Highlights

### Technical Excellence
- **Clean Architecture:** Modular, maintainable codebase
- **Type Safety:** Full TypeScript implementation
- **API Design:** RESTful endpoints with proper HTTP methods
- **Database Design:** Normalized schema with relationships
- **Error Handling:** Comprehensive validation and error management

### Feature Completeness
- **CRUD Operations:** Complete Create, Read, Update, Delete functionality
- **Business Logic:** Real-world HR processes implemented
- **Data Validation:** Client and server-side validation
- **User Experience:** Professional, intuitive interface
- **Scalability:** Architecture ready for production deployment

### Innovation & Extras
- **Real-time Dashboard:** Live statistics and analytics
- **Advanced Filtering:** Multi-parameter search system
- **Bulk Operations:** Mass data import/export capabilities
- **Notification System:** Alert and messaging framework
- **Performance Tracking:** Employee review and rating system

## 🚀 Deployment Ready

### Frontend Deployment (Vercel/Netlify)
```bash
cd frontend
npm run build
# Deploy the build folder
```

### Backend Deployment (Railway/Render/Heroku)
- Dockerfile included for containerization
- Environment variables configured
- Production settings ready
- Database migrations automated

## 📊 Sample Data

The application includes a comprehensive sample dataset:
- **5 Sample Employees** across different departments
- **30 Days of Attendance** records with realistic patterns
- **Multiple Leave Requests** in various states
- **Department Structure** with budgets and managers
- **Leave Types** with different policies

## 🔧 Development

### Running Tests
```bash
# Backend tests
cd backend
python manage.py test

# Frontend tests
cd frontend
npm test
```

### Code Quality
```bash
# Python linting
flake8 backend/

# TypeScript checking
cd frontend
npm run type-check
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues:

1. **Check the Console:** Browser console for frontend errors
2. **Check Server Logs:** Django server output for backend errors
3. **Verify Setup:** Ensure all dependencies are installed correctly
4. **Database Issues:** Run migrations if database errors occur

## 🎉 Acknowledgments

- Built with modern web technologies
- Designed for hackathon-level demonstration
- Production-ready architecture
- Comprehensive feature set for HR management

---

**Built with ❤️ for the hackathon community**# Human-Resource-Management-System-HRMS-Lite-
