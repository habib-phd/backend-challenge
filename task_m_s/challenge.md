# Django Project Setup and Run Instructions

## Setup Instructions

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


```markdown
# Starting the Django Server

To begin using the task management system, follow these steps:

1. **Run the Django Development Server:**  
   Execute the command `python manage.py runserver` in your terminal to start the Django development server.

2. **Accessing the APIs:**
   - **Task API Endpoints:**  
     - List and Create Tasks: [http://127.0.0.1:8000/api/tasks/](http://127.0.0.1:8000/api/tasks/)
     - Retrieve, Update, and Delete Task: [http://127.0.0.1:8000/api/tasks/<task_id>/](http://127.0.0.1:8000/api/tasks/<task_id>/)

   - **Label API Endpoints:**  
     - List and Create Labels: [http://127.0.0.1:8000/api/labels/](http://127.0.0.1:8000/api/labels/)
     - Retrieve, Update, and Delete Label: [http://127.0.0.1:8000/api/labels/<label_id>/](http://127.0.0.1:8000/api/labels/<label_id>/)

3. **Additional Notes:**
   - The system already contains two staff users who can perform CRUD operations on tasks and labels. You can use the following credentials to log in:
     - User 1: 
       - Username: 'user_1'
       - Password: 'User_1_api_task'
     - User 2: 
       - Username: 'user_2'
       - Password: 'User_2_api_task'

4. **Accessing the Login Page:**
   When you run the server, it will redirect you to the login page.


