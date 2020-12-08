# aluguel-de-salas

Simple Python CRUD application with Django REST Framework.

## Quick start

Create and enter a new virtual environment:
1. `python -m venv .venv`
2. `source .venv/bin/activate`

Install the project dependencies using Poetry:
- `poetry install`

Migrate the project database:
- `python manage.py migrate`

Create user to browse the API:
- `python manage.py createsuperuser --email your-email --username your-username`

Spin up the web server:
- `python manage.py runserver`
