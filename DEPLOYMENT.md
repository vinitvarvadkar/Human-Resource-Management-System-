# Deployment Guide

This guide covers deploying HRMS Lite to popular cloud platforms.

## Backend Deployment

### Option 1: Railway (Recommended)

1. **Prepare your repository:**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy to Railway:**
   - Go to [Railway.app](https://railway.app)
   - Sign up/Login with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your HRMS Lite repository
   - Railway will automatically detect the Dockerfile and deploy

3. **Configure environment variables (if needed):**
   - In Railway dashboard, go to your project
   - Click on "Variables" tab
   - Add any required environment variables

4. **Get your backend URL:**
   - Once deployed, Railway will provide a URL like `https://your-app.railway.app`

### Option 2: Render

1. **Create a new Web Service:**
   - Go to [Render.com](https://render.com)
   - Connect your GitHub repository
   - Choose "Web Service"

2. **Configure the service:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Environment: Python 3

### Option 3: Heroku

1. **Install Heroku CLI and login:**
   ```bash
   heroku login
   ```

2. **Create Heroku app:**
   ```bash
   cd backend
   heroku create your-hrms-backend
   ```

3. **Create Procfile:**
   ```
   web: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

4. **Deploy:**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

## Frontend Deployment

### Option 1: Vercel (Recommended)

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Deploy:**
   ```bash
   cd frontend
   vercel
   ```

3. **Configure environment variables:**
   - In Vercel dashboard, go to your project settings
   - Add environment variable: `REACT_APP_API_URL` = your backend URL

### Option 2: Netlify

1. **Build the app:**
   ```bash
   cd frontend
   npm run build
   ```

2. **Deploy to Netlify:**
   - Go to [Netlify.com](https://netlify.com)
   - Drag and drop the `build` folder
   - Or connect your GitHub repository for automatic deployments

3. **Configure environment variables:**
   - In Netlify dashboard, go to Site settings → Environment variables
   - Add: `REACT_APP_API_URL` = your backend URL

### Option 3: GitHub Pages

1. **Install gh-pages:**
   ```bash
   cd frontend
   npm install --save-dev gh-pages
   ```

2. **Add to package.json:**
   ```json
   {
     "homepage": "https://yourusername.github.io/hrms-lite",
     "scripts": {
       "predeploy": "npm run build",
       "deploy": "gh-pages -d build"
     }
   }
   ```

3. **Deploy:**
   ```bash
   npm run deploy
   ```

## Environment Variables

### Backend
- `DATABASE_URL`: Database connection string (optional, defaults to SQLite)
- `CORS_ORIGINS`: Allowed origins for CORS (optional)

### Frontend
- `REACT_APP_API_URL`: Backend API URL (required for production)

## Post-Deployment Checklist

1. ✅ Backend is accessible and returns JSON response at `/`
2. ✅ Frontend loads without errors
3. ✅ Frontend can communicate with backend API
4. ✅ Employee creation works
5. ✅ Attendance marking works
6. ✅ Data persists between sessions
7. ✅ CORS is properly configured
8. ✅ All forms validate correctly
9. ✅ Error handling works as expected
10. ✅ Mobile responsiveness is working

## Troubleshooting

### Common Issues

1. **CORS Errors:**
   - Ensure backend CORS_ORIGINS includes your frontend domain
   - Check that API calls use the correct backend URL

2. **API Connection Failed:**
   - Verify REACT_APP_API_URL is set correctly
   - Check that backend is running and accessible

3. **Database Issues:**
   - SQLite database will be created automatically
   - For production, consider using PostgreSQL

4. **Build Failures:**
   - Check Node.js and Python versions
   - Ensure all dependencies are listed in requirements.txt/package.json

### Getting Help

If you encounter issues:
1. Check the browser console for errors
2. Check backend logs in your deployment platform
3. Verify environment variables are set correctly
4. Test API endpoints directly using the `/docs` endpoint