import smtplib
from email.message import EmailMessage

def send_email(sender, app_password, recipient, subject, body):
    
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)

    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(sender, app_password)
    smtp.send_message(msg)
    smtp.quit()

def main():
    sender = "rid.253.python.test@gmail.com"
    app_password = "aequ urfo cuua untm"
    recipient = "khalid6101992@gmail.com"
    subject = "Test Email from python script"
    body = "Jay Ganesh"

    send_email(sender, app_password, recipient, subject, body)
    print("Email sent successfully!")

if __name__ == "__main__":
    main()