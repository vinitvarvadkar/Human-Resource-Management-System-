#!/bin/bash

# HRMS Lite Pro - PythonAnywhere Deployment Script
# Update the USERNAME variable with your PythonAnywhere username

USERNAME="yourusername"  # CHANGE THIS TO YOUR PYTHONANYWHERE USERNAME
PROJECT_PATH="/home/$USERNAME/hrms-lite"

echo "🚀 Starting HRMS Lite Pro deployment to PythonAnywhere..."

# Check if we're in the right directory
if [ ! -f "backend/manage.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

echo "📁 Setting up project structure..."

# Create necessary directories
mkdir -p $PROJECT_PATH/backend/staticfiles
mkdir -p $PROJECT_PATH/backend/logs

echo "🐍 Setting up Python virtual environment..."

# Create and activate virtual environment
python3.10 -m venv $PROJECT_PATH/venv
source $PROJECT_PATH/venv/bin/activate

echo "📦 Installing Python dependencies..."

# Install requirements
cd backend
pip install -r requirements.txt

echo "🗄️ Setting up database..."

# Run migrations
python manage.py migrate --settings=hrms_project.settings_production

echo "📊 Creating sample data..."

# Populate sample data
python populate_data.py

echo "📁 Collecting static files..."

# Collect static files
python manage.py collectstatic --settings=hrms_project.settings_production --noinput

echo "✅ Backend deployment complete!"
echo ""
echo "📋 Next steps:"
echo "1. Go to your PythonAnywhere Web tab"
echo "2. Create a new web app (Manual configuration, Python 3.10)"
echo "3. Set Source code to: $PROJECT_PATH/backend"
echo "4. Set Virtualenv to: $PROJECT_PATH/venv"
echo "5. Update WSGI file with the provided configuration"
echo "6. Set static files URL to /static/ and directory to $PROJECT_PATH/backend/staticfiles/"
echo "7. Reload your web app"
echo ""
echo "🌐 Your API will be available at: https://$USERNAME.pythonanywhere.com/api/"
echo ""
echo "For frontend deployment, see DEPLOYMENT_GUIDE.md"

echo "🎉 Deployment script completed!"