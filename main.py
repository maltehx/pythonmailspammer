import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

value = 0;
username = ""
password = ""
mail_from = ""
mail_to = ""
mail_subject = ""
mail_body = ""

print("Mail spammer  -  github/maltehx")
username = input("Your email: ")
password = input("Your password: ")
mail_from = input("Sender email: ")
mail_to = input("Mail receiver: ")
mail_subject = input("Mail subject: ")
mail_body = input("Mail Text: ")
value = input("How many mails do you want to send? ")

mimemsg = MIMEMultipart()
mimemsg['From'] = mail_from
mimemsg['To'] = mail_to
mimemsg['Subject'] = mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))
connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
connection.starttls()
connection.login(username, password)
for x in range(int(value)):
    connection.send_message(mimemsg)
    print("sent!")
    time.sleep(2)
connection.quit()