import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

my_email = EmailMessage()
my_email['from'] = 'Bob'
my_email['to'] = 'test@gmail.com'
my_email['subject'] = 'Let\'s go out'

html_template = Template(Path('templates/index.html').read_text())

html_content = html_template.substitute({'name': 'John', 'date': 'tomorrow'})

my_email.set_content(html_content, 'html')

with smtplib.SMTP(host='localhost', port=2525) as smtp:
    smtp.ehlo()
    smtp.send_message(my_email)
    print('Email sent!')
