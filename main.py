import smtplib
import ssl

#
smtp_server = 'smtp.office365.com'
port = 587
# 587 safe This is what we need
# 465 unsafe

# Sender
sender = 'demofs1@tgriebsch.onmicrosoft.com'
password = 'Goy69677'

# Receiver
receiver = 'demofs2@tgriebsch.onmicrosoft.com'
msg = """\
Subject: Hallo Thomas
From: {}
To: {}
This message was send from Python on 10.05.2010!
""".format(sender, receiver)

context = ssl.create_default_context()

"""
# unsafe
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg)
    print('It worked on 10.05.2021!')
"""


server = smtplib.SMTP(smtp_server, port)
try:
    server.ehlo()  # Say Hello
    #server.starttls(context=context)  # Encrypted Communication
    server.starttls()  # Encrypted Communication
    #server.ehlo()  # Say Hello
    server.login(sender, password)  # Anmeldung
    server.sendmail(sender, receiver, msg)
    print('It Worked again!')
except Exception as e:
    print(e)
finally:
    server.quit()

