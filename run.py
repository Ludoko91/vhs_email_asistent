import gettest as a
from emailclient import main

print("started")
i = main.email_worker()
i.get_mail_prep()
i.processing_mail()   
    
