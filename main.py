import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

value = 0
username = ""
password = ""
mail_sender = ""
mail_receiver = ""
mail_subj = ""
mail_text = ""

print("Mail spammer  -  github/maltehx")
print("Mail Username: ")
input(username)
print("Mail password:")
input(password)

username = ""
password = ""
mail_from = ""
mail_to = ""
mail_subject = ""
mail_body = ""

mimemsg = MIMEMultipart()
mimemsg['From'] = mail_from
mimemsg['To'] = mail_to
mimemsg['Subject'] = mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))
connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
connection.starttls()
connection.login(username, "")
for x in range(value):
    connection.send_message(mimemsg)
    print("sent!")
    time.sleep(2)
connection.quit()