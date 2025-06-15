import sqlite3
import secrets
from flask import render_template, request, redirect, url_for, flash, session, jsonify
from app import app, db
from models import User, Post, Comment, BankAccount
from sqlalchemy import text
from markupsafe import Markup
import html

# Generate CSRF token
def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = secrets.token_hex(16)
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token

@app.route('/')
def index():
    return render_template('index.html')

# SQL Injection Demonstrations
@app.route('/sql-injection')
def sql_injection():
    return render_template('sql_injection.html')

@app.route('/sql-injection/vulnerable', methods=['GET', 'POST'])
def sql_injection_vulnerable():
    users = []
    query = ""
    error = ""
    
    if request.method == 'POST':
        username = request.form.get('username', '')
        query = f"SELECT * FROM user WHERE username = '{username}'"
        
        try:
            # Vulnerable: Direct string concatenation
            result = db.session.execute(text(query))
            users = [dict(row._mapping) for row in result]
        except Exception as e:
            error = str(e)
    
    return render_template('sql_injection.html', 
                         users=users, 
                         query=query, 
                         error=error, 
                         mode='vulnerable')

@app.route('/sql-injection/secure', methods=['GET', 'POST'])
def sql_injection_secure():
    users = []
    query = ""
    error = ""
    
    if request.method == 'POST':
        username = request.form.get('username', '')
        query = "SELECT * FROM user WHERE username = :username"
        
        try:
            # Secure: Parameterized query
            result = db.session.execute(text(query), {'username': username})
            users = [dict(row._mapping) for row in result]
        except Exception as e:
            error = str(e)
    
    return render_template('sql_injection.html', 
                         users=users, 
                         query=query, 
                         error=error, 
                         mode='secure')

# XSS Demonstrations
@app.route('/xss')
def xss():
    comments = Comment.query.join(User).add_columns(User.username).all()
    return render_template('xss.html', comments=comments)

@app.route('/xss/clear', methods=['POST'])
def xss_clear():
    Comment.query.delete()
    db.session.commit()
    flash('All comments cleared!', 'info')
    return redirect(url_for('xss'))

@app.route('/xss/vulnerable', methods=['POST'])
def xss_vulnerable():
    content = request.form.get('content', '')
    
    # Ensure demo user and post exist
    user = User.query.filter_by(username='demo_user').first()
    if not user:
        user = User(username='demo_user', email='demo@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
    
    post = Post.query.first()
    if not post:
        post = Post(title='Demo Post', content='This is a demo post for XSS testing.', author_id=user.id)
        db.session.add(post)
        db.session.commit()
    
    # Vulnerable: Store raw content without sanitization
    # Add a marker to identify this as vulnerable content
    content_with_marker = f"[VULNERABLE] {content}"
    comment = Comment(content=content_with_marker, author_id=user.id, post_id=post.id)
    db.session.add(comment)
    db.session.commit()
    
    flash('Comment posted using vulnerable method - XSS payload will execute!', 'warning')
    return redirect(url_for('xss'))

@app.route('/xss/secure', methods=['POST'])
def xss_secure():
    content = request.form.get('content', '')
    
    # Ensure demo user and post exist
    user = User.query.filter_by(username='demo_user').first()
    if not user:
        user = User(username='demo_user', email='demo@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
    
    post = Post.query.first()
    if not post:
        post = Post(title='Demo Post', content='This is a demo post for XSS testing.', author_id=user.id)
        db.session.add(post)
        db.session.commit()
    
    # Secure: HTML escape the content
    escaped_content = html.escape(content)
    content_with_marker = f"[SECURE] {escaped_content}"
    comment = Comment(content=content_with_marker, author_id=user.id, post_id=post.id)
    db.session.add(comment)
    db.session.commit()
    
    flash('Comment posted securely - XSS payload has been neutralized!', 'success')
    return redirect(url_for('xss'))

# CSRF Demonstrations
@app.route('/csrf')
def csrf():
    # Ensure demo user exists
    user = User.query.filter_by(username='demo_user').first()
    if not user:
        user = User(username='demo_user', email='demo@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
    
    # Initialize demo bank account if it doesn't exist
    bank_account = BankAccount.query.filter_by(user_id=user.id).first()
    if not bank_account:
        bank_account = BankAccount(user_id=user.id, account_number='DEMO123456')
        db.session.add(bank_account)
        db.session.commit()
    
    return render_template('csrf.html', account=bank_account)

@app.route('/csrf/vulnerable', methods=['POST'])
def csrf_vulnerable():
    amount = float(request.form.get('amount', 0))
    to_account = request.form.get('to_account', '')
    
    # Vulnerable: No CSRF protection
    user = User.query.filter_by(username='demo_user').first()
    if user:
        bank_account = BankAccount.query.filter_by(user_id=user.id).first()
        if bank_account and bank_account.balance >= amount:
            bank_account.balance -= amount
            db.session.commit()
            flash(f'Transfer of ${amount} to {to_account} completed!', 'success')
        else:
            flash('Insufficient funds!', 'error')
    else:
        flash('Demo user not found!', 'error')
    
    return redirect(url_for('csrf'))

@app.route('/csrf/secure', methods=['POST'])
def csrf_secure():
    # Secure: Check CSRF token
    token = session.pop('_csrf_token', None)
    if not token or token != request.form.get('_csrf_token'):
        flash('CSRF token validation failed!', 'error')
        return redirect(url_for('csrf'))
    
    amount = float(request.form.get('amount', 0))
    to_account = request.form.get('to_account', '')
    
    user = User.query.filter_by(username='demo_user').first()
    if user:
        bank_account = BankAccount.query.filter_by(user_id=user.id).first()
        if bank_account and bank_account.balance >= amount:
            bank_account.balance -= amount
            db.session.commit()
            flash(f'Secure transfer of ${amount} to {to_account} completed!', 'success')
        else:
            flash('Insufficient funds!', 'error')
    else:
        flash('Demo user not found!', 'error')
    
    return redirect(url_for('csrf'))

@app.route('/csrf/reset', methods=['POST'])
def csrf_reset():
    user = User.query.filter_by(username='demo_user').first()
    if user:
        bank_account = BankAccount.query.filter_by(user_id=user.id).first()
        if bank_account:
            bank_account.balance = 1000.0
            db.session.commit()
            flash('Bank account balance reset to $1000.00!', 'info')
        else:
            flash('Bank account not found!', 'error')
    else:
        flash('Demo user not found!', 'error')
    
    return redirect(url_for('csrf'))

# Initialize demo data
@app.route('/init-demo-data')
def init_demo_data():
    # Create demo user
    if not User.query.filter_by(username='demo_user').first():
        user = User(username='demo_user', email='demo@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        
        # Create demo post
        post = Post(title='Demo Post', content='This is a demo post for XSS testing.', author_id=user.id)
        db.session.add(post)
        db.session.commit()
    
    flash('Demo data initialized!', 'success')
    return redirect(url_for('index'))
