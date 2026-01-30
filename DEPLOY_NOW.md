# 🚀 Deploy HRMS Lite Pro to PythonAnywhere NOW!

## Your Account Details
- **Username**: vinitvarvadkar
- **Your App URL**: https://vinitvarvadkar.pythonanywhere.com

## Step-by-Step Deployment (15 minutes)

### 1. Login to PythonAnywhere
1. Go to https://www.pythonanywhere.com/login/
2. Login with:
   - Username: `vinitvarvadkar`
   - Password: `mPAAiqtd3GD@tND`

### 2. Upload Your Code
**Option A: Via Git (Recommended)**
1. Click "Tasks" → "Bash" to open console
2. Run these commands:
```bash
git clone https://github.com/vinitvarvadkar/hrms-lite.git
cd hrms-lite
```

**Option B: Upload Files**
1. Click "Files" tab
2. Upload your entire project folder

### 3. Set Up Backend (In Bash Console)
```bash
# Navigate to project
cd hrms-lite

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

### 4. Create Web App
1. Go to **"Web"** tab in dashboard
2. Click **"Add a new web app"**
3. Choose **"Manual configuration"**
4. Select **"Python 3.10"**

### 5. Configure Web App Settings

#### Source Code
- **Source code**: `/home/vinitvarvadkar/hrms-lite/backend`

#### Virtual Environment
- **Virtualenv**: `/home/vinitvarvadkar/hrms-lite/venv`

#### WSGI Configuration
1. Click on WSGI configuration file link
2. **Replace ALL contents** with:
```python
import os
import sys

# Add your project directory to Python path
path = '/home/vinitvarvadkar/hrms-lite/backend'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hrms_project.settings_production')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### Static Files
1. In Web tab, scroll to "Static files" section
2. Add new static file mapping:
   - **URL**: `/static/`
   - **Directory**: `/home/vinitvarvadkar/hrms-lite/backend/staticfiles/`

### 6. Reload Web App
1. Click the big green **"Reload vinitvarvadkar.pythonanywhere.com"** button
2. Wait for reload to complete

### 7. Test Your Deployment
Visit these URLs to test:
- **API**: https://vinitvarvadkar.pythonanywhere.com/api/employees/
- **Admin**: https://vinitvarvadkar.pythonanywhere.com/admin/
- **Main API**: https://vinitvarvadkar.pythonanywhere.com/api/

### 8. Deploy Frontend (Optional)

#### Option A: Netlify (Recommended)
1. Go to https://netlify.com
2. Connect your GitHub repository
3. Build settings:
   - **Build command**: `cd frontend && npm run build`
   - **Publish directory**: `frontend/build`
4. Environment variables:
   - `REACT_APP_API_URL` = `https://vinitvarvadkar.pythonanywhere.com`

#### Option B: Serve from PythonAnywhere
```bash
# In bash console
cd /home/vinitvarvadkar/hrms-lite/frontend
npm install
npm run build
```
Then add static file mapping:
- **URL**: `/`
- **Directory**: `/home/vinitvarvadkar/hrms-lite/frontend/build/`

## 🎉 Success! Your App is Live

### Your Live URLs:
- **Backend API**: https://vinitvarvadkar.pythonanywhere.com
- **API Endpoints**: https://vinitvarvadkar.pythonanywhere.com/api/employees/
- **Django Admin**: https://vinitvarvadkar.pythonanywhere.com/admin/

### Sample Data Included:
- 5 employees across departments
- 30 days of attendance records
- Leave requests and management
- Department analytics
- Performance reviews

### Features Working:
✅ Employee Management (Add, Edit, Delete, View)
✅ Attendance Tracking with multiple statuses
✅ Leave Management with approval workflow
✅ Dashboard with real-time analytics
✅ Professional responsive UI
✅ Export/Import functionality
✅ Bulk operations
✅ Advanced filtering and search

## 🔧 Troubleshooting

### If you get errors:
1. **Check error logs** in Web tab → Error log
2. **Reload web app** after any changes
3. **Check file paths** are correct in WSGI file

### Common fixes:
```bash
# If database issues
python manage.py migrate --settings=hrms_project.settings_production

# If static files not loading
python manage.py collectstatic --settings=hrms_project.settings_production --noinput

# Check logs
tail -f /var/log/vinitvarvadkar.pythonanywhere.com.error.log
```

## 📱 Demo Your App

Your HRMS system includes:
- **Professional Dashboard** with charts and analytics
- **Complete Employee Management** system
- **Advanced Attendance Tracking**
- **Leave Management** with approval workflow
- **Responsive Design** that works on mobile
- **Export/Import** capabilities
- **Real-time Statistics**

Perfect for hackathon demonstrations! 🏆

---

**Need help?** Check the error logs in PythonAnywhere Web tab or refer to DEPLOYMENT_GUIDE.md for detailed troubleshooting.