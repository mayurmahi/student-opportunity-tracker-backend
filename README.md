🎓 Student Opportunity Tracker

A full-stack web application that helps students discover and track internships, hackathons, scholarships, jobs, and certifications — all in one place, with personalized recommendations and automated deadline reminders.

🚀 Live Demo


Frontend: https://student-opportunity-tracker-fronten.vercel.app/login


📌 Problem Statement

Students often miss out on valuable opportunities — scholarships, internships, hackathons — simply because they're scattered across dozens of websites. This platform centralizes these opportunities, lets students filter by their interests, and notifies them before deadlines pass.

✨ Features


🔐 JWT Authentication — Secure register/login system
👥 Role-Based Access Control — Separate permissions for Admins and Students
📋 Opportunity Management — Full CRUD for internships, hackathons, scholarships, jobs, and certifications
🔍 Search & Filter — Find opportunities by category or keyword
🎯 Personalized Recommendations — Opportunities matched to a student's selected interests
🌐 Real-Time Job Integration — Pulls live internship/job listings via the Adzuna API
📧 Automated Email Notifications — Welcome emails on signup and daily deadline reminders
⏰ Background Scheduler — Daily automated job (APScheduler) that checks upcoming deadlines and emails relevant users
💻 Responsive React Frontend — Clean dashboard and opportunity browser


🛠️ Tech Stack

Backend


Python, FastAPI
PostgreSQL + SQLAlchemy (ORM)
JWT (python-jose) for authentication
Passlib (bcrypt) for password hashing
APScheduler for background jobs
FastAPI-Mail for email notifications
Adzuna API for real-time job/internship data


Frontend


React.js
React Router DOM
Axios
React Toastify


Deployment


Backend: Render (with managed PostgreSQL)
Frontend: Vercel


🏗️ Architecture

student-opportunity-tracker/
├── app/
│   ├── models/          # SQLAlchemy database models
│   ├── schemas/         # Pydantic request/response schemas
│   ├── routers/         # API route handlers (auth, users, opportunities)
│   ├── services/        # Email service, Adzuna fetcher, scheduler
│   ├── utils/           # Auth utilities (JWT, password hashing)
│   ├── database.py      # DB connection & session management
│   ├── config.py        # Environment-based settings
│   └── main.py          # FastAPI app entry point
└── requirements.txt

🔑 API Endpoints

MethodEndpointDescriptionAccessPOST/auth/registerRegister a new userPublicPOST/auth/loginLogin and receive JWT tokenPublicGET/users/meGet current user profileAuthenticatedPATCH/users/me/interestsUpdate interest categoriesAuthenticatedGET/opportunities/List opportunities (with filters)AuthenticatedGET/opportunities/recommendedGet interest-based recommendationsAuthenticatedGET/opportunities/{id}Get a single opportunityAuthenticatedPOST/opportunities/Create a new opportunityAdmin onlyPUT/opportunities/{id}Update an opportunityAdmin onlyDELETE/opportunities/{id}Delete an opportunityAdmin onlyPOST/opportunities/fetch-from-apiFetch live listings from AdzunaAdmin only

Full interactive API documentation is available via Swagger UI at /docs.

⚙️ Getting Started Locally

Prerequisites


Python 3.10+
Node.js 18+
PostgreSQL


Backend Setup

bashgit clone https://github.com/yourusername/student-opportunity-tracker-backend.git
cd student-opportunity-tracker-backend
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt

Create a .env file in the root directory:

envDATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/opportunity_tracker
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_gmail_app_password
MAIL_FROM=your_email@gmail.com
ADZUNA_APP_ID=your_adzuna_app_id
ADZUNA_APP_KEY=your_adzuna_app_key

Run the server:

bashuvicorn app.main:app --reload

API will be live at http://localhost:8000 — Swagger docs at http://localhost:8000/docs.

Frontend Setup

bashgit clone https://github.com/yourusername/student-opportunity-tracker-frontend.git
cd student-opportunity-tracker-frontend
npm install
npm start

Frontend will be live at http://localhost:3000.

🎯 What I Learned

This project was built to gain hands-on experience with production-grade backend development, including:


Designing RESTful APIs with proper resource modeling
Implementing secure authentication and role-based authorization
Working with relational databases via an ORM
Integrating third-party APIs for real-world data
Building background jobs and scheduled tasks
Connecting a React frontend to a FastAPI backend end-to-end
Deploying a full-stack application to production


📄 License

This project is open source and available under the MIT License.

👤 Author

Mayur Mahindrakar
Computer Engineering Student, VIIT Pune


GitHub: @mayurmahi
LinkedIn: https://www.linkedin.com/in/mayur-mahindrakar-932092291?utm_source=share_via&utm_content=profile&utm_medium=member_android
