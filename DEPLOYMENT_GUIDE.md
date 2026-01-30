# 🚀 HRMS Lite Pro - PythonAnywhere Deployment Guide

This guide will help you deploy the HRMS Lite Pro application on PythonAnywhere.

## 📋 Prerequisites

1. **PythonAnywhere Account**: Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. **Git Repository**: Your code should be in a Git repository (GitHub, GitLab, etc.)

## 🔧 Step-by-Step Deployment

### Step 1: Upload Your Code to PythonAnywhere

1. **Open a Bash Console** on PythonAnywhere
2. **Clone your repository**:
   ```bash
   git clone https://github.com/yourusername/hrms-lite.git
   cd hrms-lite
   ```

### Step 2: Set Up Virtual Environment

```bash
# Create virtual environment
python3.10 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
cd backend
pip install -r requirements.txt
```

### Step 3: Configure Settings

1. **Update settings_production.py**:
   - Replace `yourusername` with your actual PythonAnywhere username
   - Update all file paths to match your directory structure

2. **Update wsgi.py**:
   - Replace `yourusername` with your actual PythonAnywhere username
   - Update the path to match your project location

### Step 4: Set Up Database

```bash
# Navigate to backend directory
cd /home/yourusername/hrms-lite/backend

# Activate virtual environment
source ../venv/bin/activate

# Run migrations
python manage.py migrate --settings=hrms_project.settings_production

# Create superuser (optional)
python manage.py createsuperuser --settings=hrms_project.settings_production

# Populate sample data
python populate_data.py
```

### Step 5: Collect Static Files

```bash
# Collect static files
python manage.py collectstatic --settings=hrms_project.settings_production --noinput
```

### Step 6: Configure Web App on PythonAnywhere

1. **Go to Web tab** in your PythonAnywhere dashboard
2. **Click "Add a new web app"**
3. **Choose "Manual configuration"**
4. **Select Python 3.10**
5. **Configure the following**:

#### Source Code
- **Source code**: `/home/yourusername/hrms-lite/backend`

#### Virtual Environment
- **Virtualenv**: `/home/yourusername/hrms-lite/venv`

#### WSGI Configuration File
- **Path**: `/var/www/yourusername_pythonanywhere_com_wsgi.py`
- **Replace the contents** with:

```python
import os
import sys

# Add your project directory to Python path
path = '/home/yourusername/hrms-lite/backend'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hrms_project.settings_production')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### Static Files
- **URL**: `/static/`
- **Directory**: `/home/yourusername/hrms-lite/backend/staticfiles/`

### Step 7: Deploy Frontend (Optional - Static Hosting)

For the frontend, you have several options:

#### Option 1: Serve from PythonAnywhere (Simple)
1. **Build the frontend**:
   ```bash
   cd /home/yourusername/hrms-lite/frontend
   npm install
   npm run build
   ```

2. **Configure static files** in PythonAnywhere Web tab:
   - **URL**: `/`
   - **Directory**: `/home/yourusername/hrms-lite/frontend/build/`

3. **Update frontend API URL**:
   - Create `/home/yourusername/hrms-lite/frontend/.env.production`:
   ```
   REACT_APP_API_URL=https://yourusername.pythonanywhere.com
   ```

#### Option 2: Use Netlify/Vercel (Recommended)
1. **Deploy frontend** to Netlify or Vercel
2. **Set environment variable**:
   ```
   REACT_APP_API_URL=https://yourusername.pythonanywhere.com
   ```

### Step 8: Configure CORS

Update your `settings_production.py` with the correct frontend URL:

```python
CORS_ALLOWED_ORIGINS = [
    "https://yourusername.pythonanywhere.com",
    "https://your-frontend-app.netlify.app",  # If using Netlify
    "https://your-frontend-app.vercel.app",   # If using Vercel
]
```

### Step 9: Test Your Deployment

1. **Visit your API**: `https://yourusername.pythonanywhere.com/api/employees/`
2. **Check admin panel**: `https://yourusername.pythonanywhere.com/admin/`
3. **Test frontend**: Visit your frontend URL

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. Import Errors
- **Problem**: Module not found errors
- **Solution**: Check your Python path in WSGI file and ensure virtual environment is activated

#### 2. Database Issues
- **Problem**: Database not found or permission errors
- **Solution**: 
  ```bash
  # Check database path and permissions
  ls -la /home/yourusername/hrms-lite/backend/hrms.db
  
  # If needed, recreate database
  python manage.py migrate --settings=hrms_project.settings_production
  ```

#### 3. Static Files Not Loading
- **Problem**: CSS/JS files not loading
- **Solution**: 
  ```bash
  # Recollect static files
  python manage.py collectstatic --settings=hrms_project.settings_production --noinput
  ```

#### 4. CORS Errors
- **Problem**: Frontend can't connect to backend
- **Solution**: Update `CORS_ALLOWED_ORIGINS` in `settings_production.py`

#### 5. 500 Internal Server Error
- **Problem**: Server errors
- **Solution**: Check error logs in PythonAnywhere Web tab or:
  ```bash
  tail -f /home/yourusername/hrms-lite/backend/django.log
  ```

### Useful Commands

```bash
# Restart web app (after code changes)
# Go to Web tab in PythonAnywhere dashboard and click "Reload"

# View logs
tail -f /var/log/yourusername.pythonanywhere.com.server.log
tail -f /var/log/yourusername.pythonanywhere.com.error.log

# Update code from Git
cd /home/yourusername/hrms-lite
git pull origin main

# Activate virtual environment
source venv/bin/activate

# Run migrations after updates
cd backend
python manage.py migrate --settings=hrms_project.settings_production

# Collect static files after updates
python manage.py collectstatic --settings=hrms_project.settings_production --noinput
```

## 🌐 Alternative Deployment Options

### Backend Alternatives
- **Railway**: Easy deployment with Git integration
- **Render**: Free tier with automatic deployments
- **Heroku**: Popular platform with good Django support
- **DigitalOcean App Platform**: Scalable with database options

### Frontend Alternatives
- **Netlify**: Free static hosting with CI/CD
- **Vercel**: Excellent for React apps
- **GitHub Pages**: Free hosting for static sites
- **Firebase Hosting**: Google's hosting platform

## 📚 Additional Resources

- [PythonAnywhere Django Tutorial](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
- [CORS Configuration](https://github.com/adamchainz/django-cors-headers)

## 🎉 Success!

Once deployed, your HRMS Lite Pro will be accessible at:
- **Backend API**: `https://yourusername.pythonanywhere.com/api/`
- **Admin Panel**: `https://yourusername.pythonanywhere.com/admin/`
- **Frontend**: Your chosen frontend hosting platform

Your hackathon-level HRMS system is now live and ready for demonstration!

---

**Need help?** Check the PythonAnywhere forums or Django documentation for additional support.