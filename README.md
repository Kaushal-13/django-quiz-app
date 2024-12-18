
# Django Quiz App

This is a simple Django-based quiz application. It allows a user to start a quiz session, answer multiple-choice questions, and see their score after completing the quiz.

## Features

- **Start a new quiz session**: The user can begin a new quiz session.
- **Get random questions**: A random question is pulled from the database for the user to answer.
- **Submit answers**: The user submits an answer and receives feedback on whether the answer is correct or incorrect.
- **View score**: The user can view their score, which tracks the number of correct answers out of the total questions answered.

## Prerequisites

- Python 3.x
- Django
- SQLite (default database)

## Setup

1. **Clone the Repository**

   First, clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/Kaushal-13/django-quiz-app.git
   ```

2. **Install Dependencies**

   Install the required Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Apply Migrations**

   Run the following command to apply database migrations and set up the tables:

   ```bash
   python manage.py migrate
   ```

4. **Load Initial Data**

   If you have the `initial_data.json` file (which contains the quiz questions), you can load it into the database with this command:

   ```bash
   python manage.py loaddata fixtures/initial_data.json
   ```

5. **Run the Development Server**

   Finally, start the development server by running:

   ```bash
   python manage.py runserver
   ```

6. **Access the Application**

   Open your web browser and go to `http://127.0.0.1:8000` to access the quiz application.
```
