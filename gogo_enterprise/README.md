### Gogo's Enterprise — Business Management System
 
A full-stack business management dashboard built with **Django** and **SQLite**, featuring inventory management, sales tracking, customer management, and a live analytics dashboard.
 
 ### Features
 - **Authentication** — Secure login/logout using Django's built-in auth system
- **Dashboard** — Live summary cards (total products, daily sales, low stock alerts) and recent activity feed
- **Inventory Management** — Full CRUD for products with stock level tracking, category filtering, search, and pagination
- **Sales & Reporting** — Order management with status tracking (Completed / Pending / Cancelled) and daily revenue aggregation
- **Customer Management** — Customer records with contact details and activity history
- **Settings** — Business profile configuration (name, currency, contact info, notification preferences)
---

## Project Structure
 
```
gogos_enterprise/
├── gogos_enterprise/       # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                   # Dashboard, login, settings
│   ├── models.py           # BusinessProfile model
│   ├── views.py
│   └── urls.py
├── inventory/              # Product CRUD
│   ├── models.py           # Product model
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── sales/                  # Order CRUD & reporting
│   ├── models.py           # Order model
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── customers/              # Customer CRUD
│   ├── models.py           # Customer model
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── templates/              # All HTML templates
│   ├── base.html           # Shared sidebar layout
│   ├── login.html
│   ├── core/
│   │   ├── index.html
│   │   └── settings.html
│   ├── inventory/
│   │   ├── inventory.html
│   │   └── product_form.html
│   ├── sales/
│   │   └── reporting.html
│   └── customers/
│       └── users.html
├── static/
│   └── style.css           # Global stylesheet
├── manage.py
└── db.sqlite3              # Auto-generated after first migrate
```
 
---

## Getting Started
 
### 1. Clone the repository
 
```bash
git clone https://github.com/your-username/gogos-enterprise.git
cd gogos-enterprise
```
 
### 2. Create and activate a virtual environment
 
```bash
python -m venv venv
 
# macOS / Linux
source venv/bin/activate
 
# Windows
venv\Scripts\activate
```
 
### 3. Install dependencies
 
```bash
pip install django pillow
```
 
### 4. Apply database migrations
 
```bash
python manage.py migrate
```
 
### 5. Create a superuser (admin account)
 
```bash
python manage.py createsuperuser
```
 
### 6. Run the development server
 
```bash
python manage.py runserver