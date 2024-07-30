from emailclient import get_mail as gm
from emailclient import main

data = {
    "subject": "testentwurf",
    "to": "ludoko92@gmail.com",
    "from_": "ludoko92@gmail.com",

}
mail = "testmail"

m = main.email_worker()
i = m.get_mail_prep()
print(i)