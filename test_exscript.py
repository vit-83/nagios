from Exscript.protocols import SSH2
from Exscript import Account

account = Account('nagstat', 'b@Rd&7M0n')
conn = SSH2()
conn.connect('10.2.246.6')
conn.login(account)
# ...
conn.close()

