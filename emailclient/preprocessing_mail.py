import requests
import re

from utils.quene import question_vector_queue
from llm import llm_preprocess
from utils import embedder,api_requests


llm = llm_preprocess.llm_com()

class mail_preprocessing():

    def strip_mail(self,x):

        idmail = x["id"]
        #idmail = idmail.replace("b","")
        # message strip
        body = x["Body"]
        text_n = body.replace("/n","")
        text = text_n.replace("  ","")
        #

        email_pattern = r'<(.+?)>'
        match = re.search(email_pattern, x["to"])
        if match:
            to = match.group(1)
        else:
            to = x["to"]

        email_pattern2 = r'<(.+?)>'
        match = re.search(email_pattern2, x["from"])
        if match:
            from_ = match.group(1)
        else:
            to = x["from"]

        data = {
            "id":  x["id"],
            "from_": from_,
            "to": to,
            "subject": x["Subject"],
            "message": text,

        }
        return data
    
    def question_check(self,data):
        # Good enough?
        text = data["message"]
        if "?" in text:
            return True
        else:
           exsist = llm.llm_question_exists(text)
           if "True" in exsist:
               return True
           else: 
               return False
        

        
    def question_extraction(self,data):
        text = data["message"]
        vectorlist = []
        for x in range(0,1):
            questions = llm.llm_question_extraction(text) #list of questions
            pattern = r'!.*?\?'
            match = re.findall(pattern, questions)
            questionlist = []
            for i in match:
                a = i.replace("!","")
                questionlist.append(a)
        data["questions"] = questionlist
        for question in questionlist:
            vector = embedder.create_embbeding(question)
            vectorlist.append(vector)
        data["questionvectorlist"] = vectorlist
        

        question_vector_queue.put(data)


    

    
   