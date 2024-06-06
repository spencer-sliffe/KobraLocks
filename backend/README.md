# KobraLocks Backend

The backend for the KobraLocks project is built with Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design. This backend is responsible for handling business logic, database interactions, and serving as the API for the frontend.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following tools installed:
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setting Up the Development Environment

1. **Clone the repository** (if you haven't already):

   ```bash
   git clone https://github.com/yourusername/kobralocks.git
   cd kobralocks/backend

UNIX:
python3 -m venv venv
source venv/bin/activate

WINDOWS:
python -m venv venv
venv\Scripts\activate

DEPENDENCIES:
pip install -r requirements.txt

RUN SERVER:
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
	The server will start on http://127.0.0.1:8000/. The admin panel can be accessed at http://127.0.0.1:8000/admin.


POSTGRE INSTRUCTIONS:
The PostGRESQL server is currently set up to connect to a local database hosted via local machine, to work with this set up you need to install PostGre to your local machine and it will also install pgadmin along with it, which is a GUI to work with PostGreSQL. Then after that you can create a database and the name of the database will replace the one currently there. The user and password fields will also most likely have to change on a person to person basis as of right now.
