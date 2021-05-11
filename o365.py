from O365 import Message
from O365 import Account

# Sender
sender = 'demofs1@tgriebsch.onmicrosoft.com'
password = 'Goy69677'

# Receiver
receiver = 'demofs2@tgriebsch.onmicrosoft.com'

credentials = (sender, password)

account = Account(credentials)
m = account.new_message()
m.to.add(receiver)
m.subject = 'Testing!'
m.body = "George Best quote: I've stopped drinking, but only while I'm asleep."
m.send()


