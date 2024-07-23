import smtplib, ssl
import os

def send_email(user_email, user_message):
    host = "smtp.gmail.com"
    port = 465

    username = "sender@gmail.com"
    password =  os.getenv("EMAIL_PASSWORD")


    receiver_email = user_email
    context = ssl.create_default_context()

    message = f"""Subject: Message from app2 form \n + {user_message}"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)
        
