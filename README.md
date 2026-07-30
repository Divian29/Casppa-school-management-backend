# Casppa School Management System - Backend

A Django REST API backend for managing school operations, including student admissions, parent linking, notifications, and bulk student imports.

## Features Implemented

### Students & Admissions

- Create student records
- Assign students to:
  - School
  - Class
  - House
  - Parent
- Validate duplicate admission numbers
- Maintain student history records
- Student status management

### Bulk Student Import

- Upload students using CSV
- Preview CSV data before import
- Validate imported records
- Detect:
  - Duplicate admission numbers
  - Invalid gender values
  - Missing classes
  - Missing houses
  - Missing parents
  - Invalid dates
- Flag invalid rows without blocking valid imports

## Tech Stack

- Python 3
- Django
- Django REST Framework
- SQLite/PostgreSQL
- REST API

## Project Structure


backend/
│
├── students/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── services.py
│ └── csv_import.py
│
├── parents/
├── schools/
├── notifications/
├── admissions/
└── config/


## Setup Instructions

### Clone repository

```bash
git clone <repository-url>
cd Casppa/backend
Create virtual environment
python -m venv venv

Activate:

Mac/Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Run migrations
python manage.py migrate
Start server
python manage.py runserver

API will be available at:

http://127.0.0.1:8000/
CSV Import Example

CSV format:

school,admission_number,first_name,last_name,date_of_birth,gender,class,house,parent_email
1,CAS001,John,Doe,2015-03-10,MALE,Primary 1,Red,john@example.com
API Endpoints
Create Student
POST /api/students/
Preview CSV Import
POST /api/students/import/preview/
Change Student Status
POST /api/students/{id}/change-status/
Future Improvements
Confirm CSV import endpoint
Student promotion workflow
Graduation and alumni management
Leaving certificate generation
Authentication and permissions

---

### 3. Add and commit README

Run:

```bash
git add README.md

Then:

git commit -m "Add project documentation"

Then push:

git push