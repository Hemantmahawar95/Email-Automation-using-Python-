import smtplib
import ssl
from email.message import EmailMessage

EMAIL = "Enter__Your__Gmail_"
APP_PASSWORD = "Enter__Your_App_Password"

receivers = {
    "a@gmail.com": "Hello a, your report is ready.",
    "b@gmail.com": "Hi yk, today's meeting is at 4 PM.",
    "b@gmail.com": "Hello c, your OTP is 12345."
}

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL, APP_PASSWORD)

    for receiver, text in receivers.items():
        msg = EmailMessage()
        msg["From"] = EMAIL
        msg["To"] = receiver
        msg["Subject"] = "Hello"
        msg.set_content(text)
        
        server.send_message(msg)
        print("Sent to:", receiver)

print("Done!")
