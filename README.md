# 🛡️ Web Vulnerability Lab — Learn, Simulate & Secure the Web

[![Made by Subuhana B](https://img.shields.io/badge/Made%20By-Subuhana%20B-blueviolet)](https://github.com/subuhana2303)  [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  [![Backend](https://img.shields.io/badge/Backend-Flask-blue)]()  [![Database](https://img.shields.io/badge/Database-PostgreSQL-blueviolet)]() 

> 🔐 A safe and interactive sandbox to learn how common web vulnerabilities work — and how to defend against them. Built with Flask, PostgreSQL, and Bootstrap.

---

## 🧩 Overview

**Web Vulnerability Lab** is a security-focused educational platform that demonstrates real-world attack scenarios in a safe environment. Learn how malicious users exploit vulnerabilities like SQL Injection, Cross-Site Scripting (XSS), and Cross-Site Request Forgery (CSRF), and explore secure coding strategies to prevent them.

---

## 🌟 Key Features

✅ SQL Injection (Vulnerable vs Secure Login)  
✅ Cross-Site Scripting (XSS via form input)  
✅ Cross-Site Request Forgery (Simulated Banking Transfer)  
✅ Real-time form input, execution logs, and code comparisons  
✅ One-click "Init Demo Data" setup for instant testing  
✅ Clean UI with Bootstrap dark mode  

---

## 🛠️ Tech Stack

| Layer        | Technology                            |
|--------------|----------------------------------------|
| Backend      | Python Flask, SQLAlchemy ORM           |
| Frontend     | Jinja2 + Bootstrap 5 (Dark Theme)      |
| Database     | PostgreSQL (default), SQLite (fallback)|
| Security     | CSRF Protection, Escaped Templates, Input Sanitization |


---

## 📹 Demo Walkthrough

🎬 **Watch Demo Video**: [Click to Watch on Google Drive](https://drive.google.com/file/d/1jBenpLY5WBLv6VLnZ6shxLxohKIXEVsn/view?usp=sharing)

## 🖼️ Screenshots  

## Dashboard  
![Screenshot 2025-06-15 175234](https://github.com/user-attachments/assets/e4f7d8df-6d47-4d94-85da-cdb09f63d014)

## SQL Injection  
<div align="center">
  <img src="https://github.com/user-attachments/assets/2a76322a-ba6e-4d2e-ae72-c26f9444fb14" alt="SQL Injection" width="48%">
</div>

## XSS Attack Demo  
<div align="center">
  <img src="https://github.com/user-attachments/assets/0f9de75f-50bf-43bf-8eae-9f0c87e97756" alt="XSS Attack 1" width="48%">
  <img src="https://github.com/user-attachments/assets/84751d2c-a772-4e1b-9472-0e28c38db08e" alt="XSS Attack 2" width="48%">
</div>

## CSRF Protected Transfer  
<div align="center">
  <img src="https://github.com/user-attachments/assets/4df347c6-f9d2-4a1e-9bff-17c2fce7de95" alt="CSRF Transfer" width="48%">
</div>



---

## 📁 Project Structure

```
WEB-VULNERABILITY-LAB/
├── app.py # Main Flask app
├── models.py # Database models
├── routes.py # All route logic
├── templates/ # HTML Templates (Jinja2)
├── static/ # CSS/JS files
├── screenshots/ # Screenshots for demo
├── requirements.txt # Dependencies
└── README.md

```

---

## 🚀 Getting Started Locally

### 1️⃣ Clone the Repository

git clone https://github.com/subuhana2303/web-vulnerability-lab.git
cd web-vulnerability-lab

### 2️⃣ Install Dependencies

pip install -r requirements.txt

### 3️⃣ Run the Flask App

python app.py

### ➡️ Open your browser: http://localhost:9000
🧪 Click "Init Demo Data" to populate the app and begin exploring vulnerabilities.

---
### 🧠 Sample Payloads

## 🔓 SQL Injection
```
' OR '1'='1

admin'--

' UNION SELECT 1,2,3--
```
## 🦠 XSS
```
<script>alert('XSS')</script>

<img src=x onerror=alert(1)>

<svg onload=alert('XSS')>
```
## 🎯 CSRF
```
Transfer page tested with/without tokens

Secure form prevents unauthorized requests
```
---

## 🎓 Learning Outcomes
Understand the mechanism behind common vulnerabilities

Differentiate between insecure and secure coding practices

Get hands-on with Flask, HTML templating, and security defenses

Learn how CSRF tokens and HTML escaping protect users

## 💡 Motivation
This project was created to:

Help beginners and students learn web application security

Enable safe experimentation with real-world attacks

Support academic teaching and cybersecurity awareness

---

## 🙋🏻‍♀️ About Me
 👩🏻 Subuhana B
 
 📧 subuhanabasheer41@gmail.com
 
 🌐 GitHub: @subuhana2303

---
## 🤝 Contributing
Pull requests and suggestions are welcome!
If you'd like to contribute enhancements, please fork the repo and submit a PR.
For feature ideas or bug reports, feel free to open an issue.

---

## ⚠️ Disclaimer
This project is for educational use only.
Never use these techniques in unauthorized environments. Always test within legal, ethical, and permitted boundaries.

---
## 📄 License
This project is licensed under the MIT License.
You are free to fork, use, and build on it with proper credit.

---
