# Event Management API Documentation

## Overview

The Event Management API allows users to create, update, and delete events, and view upcoming events. This API supports CRUD operations for events and users, as well as basic authentication.

## Endpoints

### User Endpoints

#### Create User

- **URL:** `/api/users/`
- **Method:** `POST`
- **Description:** Creates a new user.
- **Request Headers:**
  - `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "password123",
    "first_name": "Test",
    "last_name": "User"
  }

Response:
{
  "id": 1,
  "username": "testuser",
  "email": "testuser@example.com",
  "first_name": "Test",
  "last_name": "User"
}

Retrieve User

URL: /api/users/<id>/

Method: GET

Description: Retrieves details of a specific user.

Request Headers:

Authorization: Token <token>

Response:
{
  "id": 1,
  "username": "testuser",
  "email": "testuser@example.com",
  "first_name": "Test",
  "last_name": "User"
}

Event Endpoints
Create Event
URL: /api/events/

Method: POST

Description: Creates a new event.

Request Headers:

Content-Type: application/json

Authorization: Token <token>

Request Body:
{
  "title": "Event Title",
  "description": "Event Description",
  "date": "2024-12-31T23:59:59Z",
  "location": "Event Location"
}

Response:
{
  "id": 1,
  "title": "Event Title",
  "description": "Event Description",
  "date": "2024-12-31T23:59:59Z",
  "location": "Event Location"
}

Retrieve Event
URL: /api/events/<id>/

Method: GET

Description: Retrieves details of a specific event.

Request Headers:

Authorization: Token <token>

Response:
{
  "id": 1,
  "title": "Event Title",
  "description": "Event Description",
  "date": "2024-12-31T23:59:59Z",
  "location": "Event Location"
}

Update Event
URL: /api/events/<id>/

Method: PUT

Description: Updates an existing event.

Request Headers:

Content-Type: application/json

Authorization: Token <token>

Request Body:
{
  "title": "Updated Event Title",
  "description": "Updated Event Description",
  "date": "2024-12-31T23:59:59Z",
  "location": "Updated Event Location"
}

Response:
{
  "id": 1,
  "title": "Updated Event Title",
  "description": "Updated Event Description",
  "date": "2024-12-31T23:59:59Z",
  "location": "Updated Event Location"
}

Delete Event
URL: /api/events/<id>/

Method: DELETE

Description: Deletes an event.

Request Headers:

Authorization: Token <token>

Response: 204 No Content

List Upcoming Events

URL: /api/events/upcoming/

Method: GET

Description: Lists all upcoming events.

Request Headers:

Authorization: Token <token>

Response:
[
  {
    "id": 1,
    "title": "Event Title",
    "description": "Event Description",
    "date": "2024-12-31T23:59:59Z",
    "location": "Event Location"
  },
  {
    "id": 2,
    "title": "Another Event Title",
    "description": "Another Event Description",
    "date": "2025-01-01T00:00:00Z",
    "location": "Another Event Location"
  }
]

Authentication
The API uses token-based authentication. Users must include their token in the Authorization header for all requests that require authentication.

Obtain Token
URL: /api/token/

Method: POST


Description: Authenticates a user and returns a token.

Request Headers:

Content-Type: application/json

Request Body:
{
  "username": "testuser",
  "password": "password123"
}
Response:
{
  "token": "your_token_here"
}
Example Usage
Here is an example of how to include the token in the Authorization header:


Authorization: Token your_token_here
Setting Up the Development Environment

Clone the Repository:
git clone <repository_url>
cd <repository_directory>

Create and Activate Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies:
pip install -r requirements.txt

Run Migrations:
python manage.py migrate

Create a Superuser:
python manage.py createsuperuser

Run the Development Server:
python manage.py runserver
By following these instructions, you will be able to set up and use the Event Management API for managing events and users, as well as securing the API with token-based authentication.