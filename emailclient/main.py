import _queue
from emailclient import preprocessing_mail as proc
from emailclient import get_mail 
from emailclient import processing_mail
from utils.quene import email_queue,question_vector_queue,get_email_queue_size,get_question_vector_queue_size


prepmail = proc.mail_preprocessing()
promail = processing_mail.Processing_mail()
mail = get_mail.Mailservices()

class email_worker():

    def get_mail_prep(self):
        mail.get_mails()
        print(f"Mails-Quene size: {get_email_queue_size()}")
            #loop missing!!!!!!!!!!!!!!
        for _ in range(get_email_queue_size()):
            try:    #get one mail infos from quene
                x = email_queue.get()
            except email_queue.empty:
                print("Queue ist leer und kein Sentinel-Wert gefunden.")
            try:    #preprocess email till api call
                maildata = prepmail.strip_mail(x)
                if prepmail.question_check(maildata) is True:
                    prepmail.question_extraction(maildata) # data in Quene: question_vector_queue
                    print(f"Question-Quene size: {get_question_vector_queue_size()}")
                else:
                    print(maildata)
            except:
                print("Error with Preprocessing")
        
         
    def processing_mail(self):
        while True: 
            course = promail.call_vector_api()
            p = 0
            while True:
                mail_row = promail.write_mail(course)
                mail_check = promail.check_mail(mail_row[0],course, mail_row[1])
                p = p+1
                if mail_check is True or p == 10:
                    print("fail")
                    break
            mail.mail_to_draft(mail_row[0],course)
            if get_question_vector_queue_size() == 0:
                break
    
        
        mail.log_out()