# Secure Event Booking System - OWASP-Compliant Web Application

## 📚 Course Information
- **Course Code & Name:** IKB21503 SECURE SOFTWARE DEVELOPMENT (L01-B02)
- **Course Lecturer:** Mdm MARDIANA BINTI MAHARI
- **Submission Title:** Secure Microservice-Based Web Application with OWASP-Compliant Development Practices

## 👥 Group Members
| No. | Name | Student ID |
|-----|------|------------|
| 1 | DANISH IEMAN BIN A AZIZ | 52215124369 |
| 2 | HASIF 'IZZAT MIRZA BIN KAMAL RUZAMAN | 52215124399 |
| 3 | HARITH HAKIMI BIN MOHD FADZIL | 52215124206 |

## 📋 Project Overview
A secure web application for event booking management that implements OWASP Top 10 security controls, ASVS requirements, and secure coding best practices using Django framework.

### 🎯 CRUD Module: Event Booking System

## 🛠️ Technical Stack
- **Framework:** Django 5.0
- **Database:** SQLite 3.46.1
- **Development Environment:** VS Code 1.107.1
- **Operating System:** Kali Linux (VirtualBox)
- **Virtual Environment:** Python venv
- **Security Tools:** OWASP ZAP, Bandit, Dependency Check

## 📁 Project Structure
IKB21503_Event_Booking_Django/
├── accounts/ # User authentication & management
│ ├── migrations/ # Database migrations
│ ├── init.py
│ ├── admin.py # Django admin configuration
│ ├── apps.py # App configuration
│ ├── debug_register.py # Debug registration utilities
│ ├── models.py # User models
│ ├── tests.py # Unit tests
│ ├── urls.py # URL routing
│ └── views.py # View controllers
├── auditlog/ # Security audit logging
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py # Audit log models
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── bookings/ # Event booking CRUD operations
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── admins.py # Custom admin views
│ ├── apps.py
│ ├── models.py # Booking models
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── core/ # Django project configuration
│ ├── init.py
│ ├── asgi.py # ASGI configuration
│ ├── settings.py # Project settings (OWASP compliance)
│ ├── urls.py # Main URL routing
│ └── wsgi.py # WSGI configuration
├── templates/ # HTML templates
│ ├── accounts/ # Authentication templates
│ ├── auditlog/ # Audit log templates
│ ├── bookings/ # Booking templates
│ ├── base.html # Base template
│ ├── home.html # Home page
│ └── registration/ # Registration templates
├── static/ # Static assets
│ ├── css/ # Stylesheets
│ ├── js/ # JavaScript files
│ ├── images/ # Images
│ └── vendor/ # Third-party libraries
├── docs/ # Documentation
│ └── screenshots/ # Application screenshots
├── tests/ # Test suites
├── scripts/ # Utility scripts
├── venv/ # Python virtual environment
├── db.sqlite3 # SQLite database
├── requirements.txt # Python dependencies
├── .env.example # Environment variables template
├── fix_passwords.py # Password security utilities
└── manage.py # Django management script


## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment support

### Step 1: Clone and Setup
```bash
# Clone the project
git clone <repository-url>
cd IKB21503_Event_Booking_Django

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Step 2: Install Dependencies
```bash
bash
# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```


Step 3: Configure Environment
```bash

# Copy environment template
cp .env.example .env

# Edit .env file with your configuration
# SECRET_KEY=your-secure-key-here
# DEBUG=True
# ALLOWED_HOSTS=localhost,127.0.0.1
```

Step 4: Database Setup
```bash

# Apply database migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```


Step 5: Run the Application
```bash

# Start development server
python manage.py runserver

# Access the application at:
# http://localhost:8000/
# Admin panel: http://localhost:8000/admin/

```
