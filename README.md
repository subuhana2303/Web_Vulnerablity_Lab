# Web Vulnerability Lab

An interactive educational platform demonstrating common web security vulnerabilities and their prevention methods.

## Features

### SQL Injection Demonstration
- Interactive forms showing vulnerable vs secure database queries
- Real-time query execution with results
- Common payload examples and prevention techniques

### Cross-Site Scripting (XSS) Demo
- Vulnerable and secure comment systems
- Multiple XSS payload types (script, image, SVG)
- HTML escaping demonstration

### Cross-Site Request Forgery (CSRF) Protection
- Banking simulation with vulnerable and secure transfers
- CSRF token implementation
- Attack simulation examples

## Quick Start

1. Click "Init Demo Data" to set up sample data
2. Navigate to any vulnerability demonstration
3. Try both vulnerable and secure implementations
4. Compare code differences in the provided examples

## Educational Use

This platform is designed for:
- Web security education
- Penetration testing training
- Secure coding demonstrations
- Academic coursework

## Safety Features

- Sandboxed environment
- No real financial data
- Educational-only implementations
- Clear vulnerability warnings

## Technical Stack

- **Backend**: Python Flask with SQLAlchemy
- **Database**: PostgreSQL
- **Frontend**: Bootstrap 5 with dark theme
- **Security**: Parameterized queries, HTML escaping, CSRF tokens

## Demo Payloads

### SQL Injection
- `' OR '1'='1` - Authentication bypass
- `' UNION SELECT 1,2,3--` - Union-based attack
- `admin'--` - Comment injection

### XSS
- `<script>alert('XSS')</script>` - Basic script injection
- `<img src=x onerror=alert('XSS')>` - Image-based XSS
- `<svg onload=alert('XSS')></svg>` - SVG XSS

### CSRF
- Use the vulnerable form without protection
- Compare with secure token-protected form

## Warning

This tool is for educational purposes only. Do not use these techniques on systems you do not own or have explicit permission to test.