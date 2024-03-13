Django Project Setup and Run Instructions

Setup Instructions

1. Clone the Repository: 
   - Open your terminal.
   - Run the following command:
        "git clone https://github.com/habib-phd/backend-challenge.git"

2. Navigate to Project Directory:
   - Change directory to the project folder:
        "cd your-repository"
     
3. Database Setup:
   - Run migrations to create database tables:
        "python manage.py migrate"
     
4. Create Superuser(Optional):
   - Create a superuser to access the Django admin interface:
        "python manage.py createsuperuser"


## Running the Server

1. Start Django Server:
   - Run the Django development server:
        'python manage.py runserver'
     

2. Accessing the APIs:
    Task API Endpoints:
        List and Create Tasks: http://127.0.0.1:8000/api/tasks/
        Retrieve, Update, and Delete Task: http://127.0.0.1:8000/api/tasks/<task_id>/

    Label API Endpoints:
        List and Create Labels: http://127.0.0.1:8000/api/labels/
        Retrieve, Update, and Delete Label: http://127.0.0.1:8000/api/labels/<label_id>/

Additional Notes:
the system already have two staff user who can CRUD tasks and lebels,you can use the following data:
User 1:
    username='user_1', password='User_1_api_task'
User 2:
    username='user_2', password='User_2_api_task'
    
when you run the server it will take you to the login page.
