import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(report, to_email):
    if not report:
        return

    content = "\\n".join(f"{r['package']}: {r['current']} → {r['latest']}" for r in report)
    msg = MIMEText(content)
    msg['Subject'] = 'Outdated Python Dependencies Detected'
    msg['From'] = os.getenv("EMAIL_FROM")
    msg['To'] = to_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(os.getenv("EMAIL_FROM"), os.getenv("EMAIL_PASSWORD"))
        server.send_message(msg)
