# API Documentation

## Introduction

This API provides basic CRUD (Create, Read, Update, Delete) operations for managing "persons." It is built using Node.js, Express, and Mongoose, and connects to a MongoDB database. The API allows you to create, retrieve, update, and delete person records.

## API Base URL
The base URL for this API is `/api` .


## Standard Request Formats

### Create a Person (POST `/api`)

- Request Body Format:
  ```json
  {
    "name": "PersonName"
  }
  ```

### Get a Person (GET `/api/personId OR PersonName`)

- No request body is required.

### Update a Person (PUT `/api/personId OR PersonName`)

- Request Body Format:
  ```json
  {
    "name": "UpdatedPersonName"
  }
  ```

### Delete a Person (DELETE `/api/personId OR PersonName`)

- No request body is required.

## Standard Response Formats

### Success Response

- Status Code: 200 (OK)
- JSON Response Body:
  ```json
    "data": {
      "_id": "UniqueID",
      "name": "PersonName"
    }
  ```

### Error Response

- Status Code: 400 (Bad request).
- JSON Response Body:
  ```json
  {
    "detail": "JSON parse error - Expecting value:    line 1 column 9 (char 8)"
  }
  ```

## Sample Usage

### 1. Create a Person

**Request:**

```http
POST /api
Content-Type: application/json

{
  "name": "John Doe"
}
```

**Response (Success):**

```json  
  "data": {
    "_id": "UniqueID",
    "name": "John Doe"
  }
```

**Response (Error - Validation Failed):**

```json
{
    "detail": "JSON parse error - Expecting value: line 1 column 9 (char 8)"
}
```

### Get a Person

**Request:**

```http
GET /api/personId
```
OR
```http
GET /api/personName
```

**Response (Success):**

```json
  "data": {
    "_id": "UniqueID",
    "name": "John Doe"
  }
```

**Response (Error - Person Not Found):**

```json
{
    "detail": "Not found."
}
```

### Update a Person

**Request:**

```http
PUT /api/personId OR personName/
Content-Type: application/json

{
  "name": "Updated John Doe"
}
```

**Response (Success):**

```json
  "data": {
    "_id": "UniqueID",
    "name": "Updated John Doe"
  }
```

**Response (Error - Validation Failed):**

```json
{
    "detail": "JSON parse error - Expecting value: line 1 column 9 (char 8)"
}
```

### Delete a Person

**Request:**

```http
DELETE /api/personId OR personName/
```

**Response (Success):**

```json
{
  "detail": "Person deleted successfully!"
}
```

**Response (Error - Person Not Found):**

```json
{
  "detail": "not found"
}
```

## Known Limitations and Assumptions

- The API assumes that the `name` field is unique for each person.
- Error handling is limited to validation errors, not database-specific errors.
- The API does not support pagination for listing persons.

## Setup and Deployment

Follow these steps to set up and run the Django app locally after cloning it from GitHub:

### 1. Clone the Repository

Clone the GitHub repository to your local machine using the following command:

```bash
git clone https://github.com/timmyades3/HNG_TASK_1
```

### 2. Create a Virtual Environment

Navigate to the project directory and create a virtual environment:

```bash
cd your-django-app
python -m venv venv
```

### 3. Activate the Virtual Environment

Activate the virtual environment:

**On Windows:**

```bash
venv\Scripts\activate
```

**On macOS and Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Change the `.envexample` file in the project root to `.env`; it contains necessary environment variables. You can usually find these settings in your project's `settings.py` file.

### 6. Apply Database Migrations

Apply the database migrations to create the database schema:

```bash
python manage.py makemigrations
```

After that run:

```bash
python manage.py migrate
```

### 7. Create a Superuser (Optional)

If your app has user authentication and you want to create an admin user, run:

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The server should be accessible at `http://localhost:8000/` in your web browser.

For production deployment, consider using a production-ready web server and database setup. 
Check out [this guide](https://neon.tech/docs/guides/django) for more information.

