# Deployment Guide

## Manual Deployment (Other Platforms)


1. Set DATABASE_URL environment variable
2. Set SESSION_SECRET environment variable
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `gunicorn --bind 0.0.0.0:5000 main:app`