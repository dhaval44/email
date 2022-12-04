import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Test Mail'
email['to'] = 'testmail@mailinator.com'
email['subject'] = 'Test Mail'

email.set_content(html.substitute({'name':"XYZ"}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('newmail@gmail.com','asd123')
    smtp.send_message(email)
    print('all good')