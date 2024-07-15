# Store Visit API

## Requirements

- Python 3.11.6+
- Django 5.0.1
- Django REST Framework
- PostgreSQL or MySQL

## Installation

1. Clone the repository
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up the database in `store_visit/settings.py`
4. Run migrations:
    ```bash
    python manage.py migrate
    ```
5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

- **GET** `/api/stores/<phone_number>/`: Get a list of stores linked to the employee's phone number.
- **POST** `/api/visits/`: Create a visit to a store. Requires `Authorization: Phone <phone_number>` header.
