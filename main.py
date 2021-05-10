import smtplib
import ssl

smtp_server = 'smtp.gmail.com'
port = 465
# 587 safe
# 465 unsafe

# Sender
sender = 'sender@gmail.com'
password = 'geheim'

# Receiver
receiver = 'receiver@gmail.com'
msg = """\
Subject: Hallo Thomas
From: {}
To: {}git
This message was send from Python on 10.05.2010!
""".format(sender, receiver)

context = ssl.create_default_context()

# unsafe
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg)
    print('It worked on 10.05.2021!')

''' # safe
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # Say Hello
    server.starttls(context=context)  # Encrypted Communication
    server.ehlo()  # Say Hello
    server.login(sender, password)  # Anmeldung
    print('It Worked again!')
except Exception as e:
    print(e)
finally:
    server.quit()
'''
