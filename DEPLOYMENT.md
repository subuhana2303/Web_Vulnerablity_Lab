# Deployment Guide

## Replit Deployment

This Web Vulnerability Lab is optimized for Replit deployment.

### Steps to Deploy:

1. **Database Setup**: PostgreSQL database is already configured
2. **Environment Variables**: All required secrets are pre-configured
3. **Dependencies**: All packages are installed via pyproject.toml
4. **Server Configuration**: Gunicorn is configured for production

### Production Settings:

- **Port**: 5000 (automatically configured)
- **Host**: 0.0.0.0 (accessible from external connections)
- **Database**: PostgreSQL with connection pooling
- **Security**: CSRF protection enabled, HTML escaping active

### Post-Deployment:

1. Visit your deployed URL
2. Click "Initialize Demo Data" to set up sample data
3. Test all three vulnerability demonstrations
4. Share with students or security training participants

### Security Considerations:

- This is an educational tool demonstrating vulnerabilities
- Do not expose to production networks without proper isolation
- Regularly update dependencies for security patches
- Monitor usage for educational purposes only

### Performance:

- Optimized for educational use (10-50 concurrent users)
- Database queries are efficient with proper indexing
- Static assets served via CDN (Bootstrap, Font Awesome)

## Manual Deployment (Other Platforms)

If deploying elsewhere:

1. Set DATABASE_URL environment variable
2. Set SESSION_SECRET environment variable
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `gunicorn --bind 0.0.0.0:5000 main:app`