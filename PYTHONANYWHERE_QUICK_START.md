# 🚀 Quick Start: Deploy HRMS Lite Pro to PythonAnywhere

## 📋 Prerequisites
- PythonAnywhere account (free tier works!)
- Git repository with your HRMS code

## ⚡ Quick Deployment Steps

### 1. Upload Code to PythonAnywhere
```bash
# In PythonAnywhere Bash console
git clone https://github.com/yourusername/hrms-lite.git
cd hrms-lite
```

### 2. Set Up Backend
```bash
# Create virtual environment
python3.10 -m venv venv
source venv/bin/activate

# Install dependencies
cd backend
pip install -r requirements.txt

# Set up database
python manage.py migrate --settings=hrms_project.settings_production
python populate_data.py
python manage.py collectstatic --settings=hrms_project.settings_production --noinput
```

### 3. Configure Web App
1. Go to **Web** tab in PythonAnywhere dashboard
2. Click **"Add a new web app"**
3. Choose **"Manual configuration"** → **Python 3.10**
4. Set **Source code**: `/home/yourusername/hrms-lite/backend`
5. Set **Virtualenv**: `/home/yourusername/hrms-lite/venv`

### 4. Update WSGI File
Replace contents of WSGI file with:
```python
import os
import sys

path = '/home/yourusername/hrms-lite/backend'  # Update username
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hrms_project.settings_production')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 5. Configure Static Files
- **URL**: `/static/`
- **Directory**: `/home/yourusername/hrms-lite/backend/staticfiles/`

### 6. Update Settings
Edit `backend/hrms_project/settings_production.py`:
- Replace `yourusername` with your actual username
- Update all file paths

### 7. Reload Web App
Click **"Reload"** button in Web tab

## 🌐 Access Your App
- **API**: `https://yourusername.pythonanywhere.com/api/employees/`
- **Admin**: `https://yourusername.pythonanywhere.com/admin/`

## 🎨 Deploy Frontend (Optional)

### Option 1: Netlify (Recommended)
1. Connect your GitHub repo to Netlify
2. Set build command: `cd frontend && npm run build`
3. Set publish directory: `frontend/build`
4. Add environment variable: `REACT_APP_API_URL=https://yourusername.pythonanywhere.com`

### Option 2: Serve from PythonAnywhere
```bash
cd /home/yourusername/hrms-lite/frontend
npm install
npm run build
```
Then add static files mapping:
- **URL**: `/`
- **Directory**: `/home/yourusername/hrms-lite/frontend/build/`

## 🔧 Troubleshooting

### Common Issues:
1. **Import errors**: Check WSGI file paths
2. **Database errors**: Run migrations again
3. **Static files not loading**: Run collectstatic again
4. **CORS errors**: Update CORS_ALLOWED_ORIGINS in settings

### Useful Commands:
```bash
# View logs
tail -f /var/log/yourusername.pythonanywhere.com.error.log

# Update code
cd /home/yourusername/hrms-lite
git pull origin main

# Restart after changes
# Go to Web tab and click "Reload"
```

## 🎉 Success!
Your HRMS Lite Pro is now live on PythonAnywhere!

**Demo Data Included:**
- 5 sample employees
- 30 days of attendance records
- Leave requests and types
- Department structure

**Features Working:**
- Employee management
- Attendance tracking
- Leave management
- Dashboard analytics
- Professional UI

Perfect for hackathon demonstrations! 🏆