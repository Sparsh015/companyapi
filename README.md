# Company API

A RESTful API project built using Django and Django REST Framework to manage companies and employees.

## Features
- CRUD APIs for Companies and Employees
- Django REST Framework ViewSets & Routers
- HyperlinkedModelSerializer
- Custom API Actions
- SQLite Database Integration
- Django Admin Customization
- Employee filtering by company
- Browsable REST API Interface
- also Learned Postman

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite

## API Endpoints

### Companies
- `GET /api/v1/companies/`
- `POST /api/v1/companies/`
- `GET /api/v1/companies/{id}/`
- `PUT /api/v1/companies/{id}/`
- `DELETE /api/v1/companies/{id}/`

### Employees
- `GET /api/v1/employees/`
- `POST /api/v1/employees/`
- `GET /api/v1/employees/{id}/`
- `PUT /api/v1/employees/{id}/`
- `DELETE /api/v1/employees/{id}/`

### Custom Endpoint
- `GET /api/v1/companies/{id}/employees/`

## Run Project

```bash
git clone https://github.com/Sparsh015/companyapi.git
cd companyapi

(mac)
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

## Learning Outcomes
- REST API Development
- Django ORM
- Serializers
- ViewSets
- Routers
- CRUD Operations
- Model Relationships
- API Testing with Postman
- Django Admin
