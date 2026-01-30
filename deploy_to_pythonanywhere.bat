@echo off
echo 🚀 HRMS Lite Pro - PythonAnywhere Deployment Preparation
echo.
echo This script prepares your project for PythonAnywhere deployment.
echo.

REM Check if we're in the right directory
if not exist "backend\manage.py" (
    echo ❌ Error: Please run this script from the project root directory
    pause
    exit /b 1
)

echo 📋 Deployment preparation checklist:
echo.
echo ✅ 1. Requirements.txt updated with production dependencies
echo ✅ 2. Production settings file created
echo ✅ 3. WSGI configuration file created
echo ✅ 4. Deployment guide created
echo.
echo 📝 Manual steps required:
echo.
echo 1. Upload your project to PythonAnywhere using Git:
echo    git clone https://github.com/yourusername/hrms-lite.git
echo.
echo 2. Run the deployment commands on PythonAnywhere:
echo    cd hrms-lite
echo    python3.10 -m venv venv
echo    source venv/bin/activate
echo    cd backend
echo    pip install -r requirements.txt
echo    python manage.py migrate --settings=hrms_project.settings_production
echo    python populate_data.py
echo    python manage.py collectstatic --settings=hrms_project.settings_production --noinput
echo.
echo 3. Configure your web app in PythonAnywhere dashboard
echo.
echo 📖 See DEPLOYMENT_GUIDE.md for detailed instructions
echo.
echo 🎉 Your project is ready for PythonAnywhere deployment!
echo.
pause