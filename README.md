# HNG 13 Stage 0 — Profile + Cat Fact API
Overview

A simple Django REST Framework API that returns my profile information along with a dynamic cat fact fetched from the Cat Facts API.

Endpoint

GET /me

Example Response
{
  "status": "success",
  "user": {
    "email": "youremail@example.com",
    "name": "Your Full Name",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-18T12:34:56.789Z",
  "fact": "Cats sleep for 70% of their lives."
}

🚀 Running Locally
1. Clone this repo
git remote add origin https://github.com/owoaanu/hng-state-zero.git
cd stage0-django-api

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables

Create a .env file in the root directory:

EMAIL=youremail@example.com
NAME=Your Full Name
STACK=Python/Django
CATFACT_API_URL=https://catfact.ninja/fact

5. Run the server
python manage.py runserver


Then visit (browser,postman,insomnia, etc):
 http://127.0.0.1:8000/me

🧩 Dependencies

Django

Django REST Framework

python-dotenv

requests

gunicorn (for deployment)

🌐 Environment Variables
Variable	Description	Example
EMAIL	Your email address	me@example.com
NAME	Your full name	John Doe
STACK	Backend stack	Python/Django
CATFACT_API_URL	Cat Facts API URL	https://catfact.ninja/fact
🧪 Tests

You can test the endpoint using:

curl http://127.0.0.1:8000/me

📝 Notes

If the external Cat Facts API fails, the endpoint returns a fallback message like:

"Could not fetch cat fact at the moment."

🌍 Deployment

Hosted on Railway:
👉 https://hng-state-zero-production.up.railway.app/me

🧑‍💻 Author

Your Name
Email: youremail@example.com
Stack: Python/Django