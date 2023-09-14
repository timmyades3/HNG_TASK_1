# HNG_TASK_1

## Table of Contents

- [View live](##view-live)
- [Local Development Setup](#Local-Development-Setup)
  - [Clone-the-Repository](#1.Clone-the-Repository)
  - [Create a Virtual Environment](#2.-Create-a-Virtual-Environment)
  - [Activate the Virtual Environment](#3.-Activate-the-Virtual-Environment)
  - [Install Dependencies](#4.-Install-Dependencies)
  - [Configure Environment Variables](#5.-Configure-Environmen-Variables)
  - [Create a Superuser (Optional)](#7.-Create-a-Superuser-(Optional))
  - [Apply Database Migrations](#6.-Apply-Database-Migrations)
  - [Run the Development Server](#8Run-the-Development-Server)
- [Endpoints](#endpoints)
- [Usage](#usage)
- [Sample Requests and Responses](#sample-requests-and-responses)
- [Contributing](#contributing)


- [Usage](#usage)

## View live
 
 https://hng-task-1-2xlb.onrender.com/api/

## Local Development Setup

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

change the `.envexample` file in the project root  to `.env`, it contains necessary environment variables. You can usually find these settings in your project's `settings.py` file.



### 6. Apply Database Migrations

Apply the database migrations to create the database schema:

```bash
python manage.py makemigrations
```
After that run 
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

## Endpoint 

- create `/api`
- read `/api`
- update `/api/personid` OR `/api/personname`
- create `/api/personid` OR `/api/personname`

## Usage

The API is designed to manage persons. You can create, retrieve, update, and delete persons using the provided endpoints.

## Sample Requests and Responses

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

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.
