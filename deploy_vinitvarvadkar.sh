#!/bin/bash
# Personalized deployment script for vinitvarvadkar on PythonAnywhere

echo "🚀 HRMS Lite Pro - PythonAnywhere Deployment Script"
echo "Username: vinitvarvadkar"
echo "=========================================="

# Step 1: Clone repository (run this in PythonAnywhere Bash console)
echo "📥 Step 1: Clone your repository"
echo "git clone https://github.com/vinitvarvadkar/hrms-lite.git"
echo "cd hrms-lite"
echo ""

# Step 2: Set up virtual environment
echo "🐍 Step 2: Set up Python environment"
echo "python3.10 -m venv venv"
echo "source venv/bin/activate"
echo ""

# Step 3: Install backend dependencies
echo "📦 Step 3: Install dependencies"
echo "cd backend"
echo "pip install -r requirements.txt"
echo ""

# Step 4: Set up database
echo "🗄️ Step 4: Set up database"
echo "python manage.py migrate --settings=hrms_project.settings_production"
echo "python populate_data.py"
echo "python manage.py collectstatic --settings=hrms_project.settings_production --noinput"
echo ""

# Step 5: Web app configuration
echo "🌐 Step 5: Configure Web App in PythonAnywhere Dashboard"
echo "1. Go to Web tab"
echo "2. Add new web app -> Manual configuration -> Python 3.10"
echo "3. Source code: /home/vinitvarvadkar/hrms-lite/backend"
echo "4. Virtualenv: /home/vinitvarvadkar/hrms-lite/venv"
echo "5. WSGI file: Replace contents with the wsgi.py from this project"
echo "6. Static files:"
echo "   URL: /static/"
echo "   Directory: /home/vinitvarvadkar/hrms-lite/backend/staticfiles/"
echo ""

# Step 6: Test deployment
echo "✅ Step 6: Test your deployment"
echo "API: https://vinitvarvadkar.pythonanywhere.com/api/employees/"
echo "Admin: https://vinitvarvadkar.pythonanywhere.com/admin/"
echo ""

echo "🎉 Your HRMS Lite Pro will be live at:"
echo "https://vinitvarvadkar.pythonanywhere.com"
echo ""
echo "📚 For detailed instructions, see DEPLOYMENT_GUIDE.md"