import time

from emailclient import main

time.sleep(4)
print("started")
i = main.email_worker()
i.get_mail_infos()