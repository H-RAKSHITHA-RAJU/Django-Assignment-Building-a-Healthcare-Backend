# Django Healthcare Backend API

This is a backend API for a healthcare application, built with Django REST Framework and PostgreSQL. This project was completed as a technical assignment.

It provides secure, JWT-authenticated endpoints for managing users, patients, and doctors.

## Getting Started: How to Run the Project

Follow these steps to get the application running locally.

### 1. Prerequisites

-   Python 3.10+
-   PostgreSQL server

### 2. Setup

-   **Clone the repository:**
    ```bash
    git clone https://github.com/H-RAKSHITHA-RAJU/Django-Assignment-Building-a-Healthcare-Backend.git
    cd Django-Assignment-Building-a-Healthcare-Backend
    ```

-   **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

-   **Configure your environment:**
    -   Create a database in PostgreSQL for this project.
    -   Copy the example environment file: `cp .env.example .env`
    -   Edit the new `.env` file with your database credentials and a `SECRET_KEY`.

### 3. Run the Server

-   **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

-   **Start the server:**
    ```bash
    python manage.py runserver
    ```

The API is now running at `http://127.0.0.1:8000/`.

---

## API Endpoints

Use an API client like Postman to test the endpoints.

### Authentication

-   `POST /api/auth/register/` - Register a new user.
-   `POST /api/auth/login/` - Log in to get a JWT access token.

### Patient Management (Authentication Required)

-   `GET, POST /api/patients/`
-   `GET, PUT, DELETE /api/patients/<id>/`

### Doctor Management (Authentication Required)

-   `GET, POST /api/doctors/`
-   `GET, PUT, DELETE /api/doctors/<id>/`

### Patient-Doctor Mappings (Authentication Required)

-   `GET, POST /api/mappings/`
-   `GET /api/mappings/<patient_id>/`
-   `DELETE /api/mappings/<id>/`
