import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Test Mail'
email['to'] = 'testmail@mailinator.com'
email['subject'] = 'Test Mail'

email.set_content('I am Mail Tester')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('newmail@gmail.com','asd123')
    smtp.send_message(email)
    print('all good')