from emailclient import processing_mail as proc
from emailclient import get_mail as mail

class email_worker():

    def get_mail_infos(self):
        mail.get_mails()
        i = proc.mail_processing()
        email_row = i.strip_mail()
        text = i.create_embbeding(email_row["message"])
        email_row["message_vector"] = text
        subject_vector = i.create_embbeding(email_row["message"])
        email_row["subject_vector"] = subject_vector
        print(email_row)