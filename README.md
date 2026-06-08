# Phone Specifications Django Project

## Description
Django project that runs a Playwright script to collect the phone's specifications
from the website and stores them in the PostgreSQL database. It takes about 5 min to collect the data.
All specs are also shown on index page.

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
