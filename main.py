import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

value = 3
username = "YOUR EMAIL"
password = "YOUR PASSWORD"
mail_from = username
mail_to = "MAIL RECEIVER"
mail_subject = "MAIL SUBJECT"
mail_body = "MAIL TEXT"

print("Mail spammer - github/maltehx")

mimemsg = MIMEMultipart()
mimemsg['From'] = mail_from
mimemsg['To'] = mail_to
mimemsg['Subject'] = mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))
connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
connection.starttls()
connection.login(username, password)
for x in range(value):
    connection.send_message(mimemsg)
    print("sent!")
    time.sleep(2)
connection.quit()