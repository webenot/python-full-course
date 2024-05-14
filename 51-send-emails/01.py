import smtplib
from email.message import EmailMessage

my_email = EmailMessage()
my_email['from'] = 'Bob'
my_email['to'] = 'test@gmail.com'
my_email['subject'] = 'Hello from Python'
my_email.set_content('Hey! How are you doing?')

with smtplib.SMTP(host='localhost', port=2525) as smtp:
    smtp.ehlo()
    # smtp.starttls()
    # smtp.login('username', 'password')
    smtp.send_message(my_email)
    print('Email sent!')
