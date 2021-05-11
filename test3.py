import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
'''
username = 'demofs1@tgriebsch.onmicrosoft.com'
password = 'Goy69677'


mail_from = username
mail_to = 'demofs2@tgriebsch.onmicrosoft.com'
mail_subject = "Test Subject"
mail_body = "This is a test message"

mimemsg = MIMEMultipart()
mimemsg['From']=mail_from
mimemsg['To']=mail_to
mimemsg['Subject']=mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))
connection = smtplib.SMTP(host='smtp.office365.com', port=587)
connection.starttls()
connection.login(username,password)
connection.send_message(mimemsg)
connection.quit()
'''