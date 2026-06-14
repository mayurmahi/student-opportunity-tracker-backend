from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.config import settings

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)

async def send_welcome_email(email: str, name: str):
    message = MessageSchema(
        subject="Welcome to Student Opportunity Tracker!",
        recipients=[email],
        body=f"""
        Hi {name},

        Welcome to Student Opportunity Tracker!
        You can now browse internships, hackathons, scholarships and more.

        Login here: http://localhost:8000/docs

        Team SOT
        """,
        subtype="plain"
    )
    fm = FastMail(conf)
    await fm.send_message(message)

async def send_deadline_reminder(email: str, name: str, opportunities: list):
    opp_list = "\n".join([f"- {opp.title} (Deadline: {opp.deadline.strftime('%d %b %Y')})" for opp in opportunities])
    message = MessageSchema(
        subject="Upcoming Deadlines - Student Opportunity Tracker",
        recipients=[email],
        body=f"""
        Hi {name},

        These opportunities are closing in 3 days:

        {opp_list}

        Login to apply: http://localhost:8000/docs

        Team SOT
        """,
        subtype="plain"
    )
    fm = FastMail(conf)
    await fm.send_message(message)