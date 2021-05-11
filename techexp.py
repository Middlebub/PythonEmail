import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

username = "demofs1@tgriebsch.onmicrosoft.com"
password = "Goy69677"
port = 587
host = 'smtp.office365.com'

mail_from = username
mail_to = "demofs2@tgriebsch.onmicrosoft.com"
mail_subject = "Test Subject for fs2 again"
mail_body = "This is a test message to fs2 again"
mail_attachment = "bigmac.pdf"
mail_attachment_name = "bigmac.pdf"


mimemsg = MIMEMultipart()
mimemsg['From'] = mail_from
mimemsg['To'] = mail_to
mimemsg['Subject'] = mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))

with open(mail_attachment, "rb") as attachment:
    mimefile = MIMEBase('application', 'octet-stream')
    mimefile.set_payload(attachment.read())
    encoders.encode_base64(mimefile)
    mimefile.add_header('Content-Disposition', "attachment; filename= %s" % mail_attachment_name)
    mimemsg.attach(mimefile)
    connection = smtplib.SMTP(host, port)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mimemsg)
    connection.quit()