

from utils.quene import question_vector_queue,get_question_vector_queue_size
from utils import api_requests
from llm import llm_processing 

api = api_requests.api_call_vec()
llm = llm_processing.llm_comm()

class Processing_mail():


    def call_vector_api(self):
        course = question_vector_queue.get()
        for question in course["questionvectorlist"]:
            #makes vector search per api call
            answers = api.send_vector(question) # gives all infos of x courses
            answer =[]
            if answers is not None:
                answermail = llm.llm_question_answering(course,answers)
                answer.append(answermail)
            else:
                print(f"answer mail is None")
        course["answers"] = answer
        return course
    
    def write_mail(self,course):
        mail = course["message"]
        answer = course["answers"]
        mail_answer= llm.llm_mail_writting(mail,answer)
        return mail_answer,mail

    def check_mail(self,mail_row,courses,answers):
        q_check = llm.llm_mail_check_q(mail_row,answers)
        for course in courses:
            fact_check = llm.llm_mail_check_facts(mail_row,course)
            if "True" in fact_check:
                fact_checks = True
            else:
                fact_checks = False
                break
        if fact_checks is True:
            if "True" in q_check:
                return True
        else:
            return False
        
                    
            