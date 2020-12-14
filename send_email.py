import smtplib

SENDER_EMAIL = "lalithbandaru36@gmail.com"
SENDER_PASSWORD = "Lbandaru389281!"

def send_email(reciever_email, subject, body):
    message = "Subject: {}\n\n{}".format(subject, body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, reciever_email, message)