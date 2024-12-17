# Quiz App

This is a Django-based quiz application.

## Features
1. Start new quiz session.
2. Get a random multiple choice question from a set of questions in database
3. Submit answer and
4. Get the total questions answered by user with details on correct and incorrect submission.

## Prerequisites

Before you start, ensure you have the following installed on your machine:

- Python 3.12 or higher
- `pip` (Python's package installer)
- PostgreSQL (if using PostgreSQL as the database)
- A code editor (such as VSCode)

## Setting Up the Project Locally

Follow these steps to get the project up and running:

### Step 1: Clone the Repository

- First, clone the repository to your local machine:

```bash
git clone https://github.com/rtnAyush/quiz_app.git
cd quiz_app
```

### Step 2: Create a Virtual Environment
- It is recommended to use a virtual environment to manage dependencies. To create and activate the virtual environment, run the following:

- Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
- macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install the Required Dependencies
- Install the dependencies listed in requirements.txt:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up the Database
- Ensure you have PostgreSQL installed and running on your machine.

- Create a new database:

```bash
createdb quiz_db
```
- Update the database settings in settings.py:

- Update the DATABASES setting in settings.py to match your PostgreSQL database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'quiz_db',  # Replace with your DB name
        'USER': 'your_db_user',  # Replace with your DB username
        'PASSWORD': 'your_db_password',  # Replace with your DB password
        'HOST': 'localhost',
        'PORT': '5432',  # Default PostgreSQL port
    }
}
```
### Step 5: Set Up Environment Variables
- If using environment variables, create a .env file in the root directory of your project with the following content:

```env
DATABASE_URL=postgres://your_db_user:your_db_password@localhost/quiz_db
```
### Step 6: Run Migrations
- Apply database migrations to create the required tables:

```bash
python manage.py migrate
```
### Step 7: Create a Superuser
- To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```
- Follow the prompts to set up the superuser account.

### Step 8: Run the Development Server
- Start the development server:

```bash
python manage.py runserver
```
- The server will be available at http://127.0.0.1:8000/.


### Step 9: Access the Application
- Open your browser and go to http://127.0.0.1:8000/ to access the application.
- To access the admin panel, go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials.