# IKB21503_Event_Booking_django

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
├── accounts/                # User authentication & management
│   ├── admin.py             # Django admin configuration for accounts
│   ├── apps.py              # App configuration for accounts
│   ├── debug_register.py    # Debug utilities for user registration
│   ├── __init__.py          # Marks this directory as a Python package
│   ├── migrations/          # Database migration files for accounts
│   ├── models.py            # User models (custom user fields, profiles)
│   ├── __pycache__/         # Compiled Python cache files
│   ├── tests.py             # Unit tests for accounts app
│   ├── urls.py              # URL routing for accounts views
│   └── views.py             # View controllers (login, register, profile)
├── auditlog/                # Security audit logging
│   ├── admin.py             # Admin configuration for audit logs
│   ├── apps.py              # App configuration for auditlog
│   ├── __init__.py          # Marks this directory as a Python package
│   ├── migrations/          # Database migration files for auditlog
│   ├── models.py            # Audit log models (track sensitive actions)
│   ├── __pycache__/         # Compiled Python cache files
│   ├── tests.py             # Unit tests for auditlog app
│   ├── urls.py              # URL routing for auditlog views
│   └── views.py             # View controllers for audit log display
├── bookings/                # Event booking CRUD operations
│   ├── admin.py             # Admin configuration for bookings
│   ├── apps.py              # App configuration for bookings
│   ├── __init__.py          # Marks this directory as a Python package
│   ├── migrations/          # Database migration files for bookings
│   ├── models.py            # Booking models (events, reservations)
│   ├── __pycache__/         # Compiled Python cache files
│   ├── tests.py             # Unit tests for bookings app
│   ├── urls.py              # URL routing for booking views
│   └── views.py             # View controllers (create, update, delete bookings)
├── core/                    # Django project configuration
│   ├── asgi.py              # ASGI configuration (async server)
│   ├── __init__.py          # Marks this directory as a Python package
│   ├── __pycache__/         # Compiled Python cache files
│   ├── settings.py          # Project settings (security, DB, middleware)
│   ├── urls.py              # Main URL routing for the project
│   └── wsgi.py              # WSGI configuration (production server)
├── db.sqlite3               # SQLite database (default dev DB)
├── fix_passwords.py         # Utility script for password security fixes
├── manage.py                # Django management script (runserver, migrate, etc.)
├── readme.md                # Project documentation (overview, setup instructions)
├── requirements.txt         # Python dependencies list
├── static/                  # Static assets (CSS, JS, vendor libraries)
│   ├── css/                 # Stylesheets
│   ├── js/                  # JavaScript files
│   └── vendor/              # Third-party libraries
├── staticfiles/             # Collected static files (after `collectstatic`)
│   ├── admin/               # Django admin static assets
│   ├── css/                 # Stylesheets
│   └── js/                  # JavaScript files
├── templates/               # HTML templates
│   ├── accounts/            # Templates for authentication (login, register)
│   ├── admin/               # Templates for admin dashboard
│   ├── app_base.html        # Base template for app-specific pages
│   ├── auditlog/            # Templates for audit log views
│   ├── base.html            # Global base template (extends site-wide)
│   ├── bookings/            # Templates for booking CRUD
│   ├── home.html            # Home page template
│   └── registration/        # Templates for registration workflows
├── tests/                   # Global test suites
└── venv/                    # Python virtual environment
    ├── bin/                 # Executables for virtual environment
    ├── include/             # C headers for compiling packages
    ├── lib/                 # Python libraries installed in venv
    ├── lib64 -> lib         # Symlink to lib
    └── pyvenv.cfg           # Virtual environment configuration file



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


