from openai import OpenAI
from gettest import i

class llm_comm():
    def __init__(self) -> None:
        self.llm_url = "https://znz9hiogu3xd72-8000.proxy.runpod.net/v1"
        self.model = "NousResearch/Meta-Llama-3-8B-Instruct"

    def llm_question_answering(self,course,answers):

        mail = course["questions"]
        text = [coursedata['description'] for coursedata in answers]

        prompt = f"Beantworte diese Frage({mail}) mit folgenden Informationen: {text}"
        try:
            client = OpenAI(
                base_url=self.llm_url,
                api_key="token-abc123",
            )

            completion = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Du beantwortest Fragen" },
                {"role": "user", "content": prompt}
            ],
            )
            answer = completion.choices[0].message.content

            return answer
        except:
            print("Error with LLM qestion answering")

    def llm_mail_writting(self,mail,answers):


        prompt = f"Beantorte diese Mail({mail}) mit folgenden Frage-Antwort-Paaren:{answers} und unterschreibe diese mit Ihr VHS-Team."

        try:
            client = OpenAI(
                base_url=self.llm_url,
                api_key="token-abc123",
            )

            completion = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Du bist ein kompetenter Mitarbeiter im Support, der fröhlich Mails  beantwortet" },
                {"role": "user", "content": prompt}
            ],
            )
            answer = completion.choices[0].message.content

            return answer
        except:
            print("Error with LLM mail writting")

    def llm_mail_check_q(self,mail_row,answers):

        # check if questions answer correctly and if facts are right!!!!

        
        prompt = f"Wurde diese Mail:({mail_row}) mit folgenden Antworten richtig beantworten? {answers} ,wenn ja antworte mit True"

        try:
            client = OpenAI(  
                base_url=self.llm_url,
                api_key="token-abc123",
            )

            completion = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Du bist ein kompetenter Mitarbeiter im Support, der überprüft, ob die mails richtig beantwortet wurden" },
                {"role": "user", "content": prompt}
            ],
            )
            answer = completion.choices[0].message.content

            return answer
        except:
            print("Error with LLM question check")

    def llm_mail_check_facts(self,mail,answers):

        # check if questions answer correctly and if facts are right!!!!

        
        prompt = f"Ist diese Mail mit den gegebenen Fakten korrekt? Mail:{mail} Fakten:{answers} ,wenn ja antworte mit True"

        try:
            client = OpenAI(  
                base_url=self.llm_url,
                api_key="token-abc123",
            )

            completion = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Du bist ein kompetenter Mitarbeiter im Support, der überprüft, ob die mails richtig beantwortet wurden" },
                {"role": "user", "content": prompt}
            ],
            )
            answer = completion.choices[0].message.content

            return answer
        except:
            print("Error with LLM facts check")