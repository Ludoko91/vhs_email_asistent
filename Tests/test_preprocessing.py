from Tests.testdata import question_vector_queue
from utils.quene import email_queue,search_obj_queue,get_email_queue_size,get_question_vector_queue_size
from emailclient import preprocessing_mail as proc

prepmail = proc.mail_preprocessing()

try:    #preprocess email till api call
    maildata = prepmail.strip_mail(question_vector_queue)
    if prepmail.question_check(maildata) is True:
        prepmail.question_extraction(maildata) # data in Quene: question_vector_queue
        print(f"Question-Quene size: {get_question_vector_queue_size()}")
finally:
    print("done")