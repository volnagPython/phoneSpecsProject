# Phone Specifications Django Project

## Description
Django project that runs a Playwright script to collect phone specifications
and stores them in PostgreSQL.

## Tech stack
- Python
- Django
- Playwright
- PostgreSQL

## Setup
```bash
git clone <repo_url>
cd phoneSpecsProject
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
python manage.py migrate
python manage.py runserver
