# Algobulls_Assignment
Visit the below link and provide admin user credentials in the alert prompt to see REST API. <br/>
Deployment link: https://dee777.pythonanywhere.com/api/todo/ <br/>
Postman Workspace: https://www.postman.com/flight-physicist-9054540/workspace/public/overview

## Admin User Credintials

Username: dee777 <br/>
Password: 1234

## Requirements

Make sure you have the following software installed on your machine:
- Python 3.10
- Django 4.2.2
- Django REST Framework 3.14

## Installation

1. Clone the repository:

   ```shell
   git clone git@github.com:dee077/Algobulls_Assignment.git

2. Setup Virtual env:

   ```shell
   pip install virtualenv 
   virtualenv env 
   source env/bin/activate  

3. Install Dependencies:

   ```shell
   cd Algobulls_Assignment
   pip install -r requirements.txt

4. Runserver

   ```shell
   python manage.py runserver

Access the application by visiting http://localhost:8000/api/todo and providing admin user password credentials in your web browser.

## API Endpoints
The project exposes the following API endpoints:
   1. GET /api/todo/: Retrieves a list of all ToDo items.
   2. POST /api/todo/: Creates a new ToDo item.
   3. GET /api/todo/{id}/: Retrieves a specific ToDo item by ID.
   4. PUT /api/todo/{id}/: Updates a specific ToDo item by ID.
   5. DELETE /api/todo/{id}/: Deletes a specific ToDo item by ID.
   6. For detailed documentation of the API endpoints and request/response examples, refer to the API documentation. <br/>

Postman Workspace: https://www.postman.com/flight-physicist-9054540/workspace/public/overview
