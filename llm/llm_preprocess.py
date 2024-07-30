from openai import OpenAI

class llm_com():
    def __init__(self) -> None:
        self.llm_url = "https://znz9hiogu3xd72-8000.proxy.runpod.net/v1"
        self.model = "NousResearch/Meta-Llama-3-8B-Instruct"

    def llm_question_extraction(self,text):

        prompt = f"Finde alle Fragen im Text und formuliere sie so um, dass der Kontext berücksichtigt wird {text}  Setze vor jede Frage ein !"

        try:
            client = OpenAI(
                base_url=self.llm_url,
                api_key="token-abc123",
            )

            completion = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Du extrahierst Fragen aus Email Texten" },
                {"role": "user", "content": prompt}
            ],
            )
            list_string = completion.choices[0].message.content
                        
            


            return list_string
        except:
            print("Error with LLM sum up")

    def llm_question_exists(self,text):

        prompt = f"Enthält diese Mail eine oder mehrere Fragen? Wenn ja gebe True zurück: {text}"

        try:
            client = OpenAI(
                base_url=self.llm_url,
                api_key="token-abc123",
            )

            completion = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Du extrahierst Fragen aus Email Texten" },
                {"role": "user", "content": prompt}
            ],
            )
            list_string = completion.choices[0].message.content
                        
            


            return list_string
        except:
            print("Error with LLM sum up")
