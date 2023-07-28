import os
import openai

class Llm:
    
    def __init__(self, delimiter, system_message, user_message,
                 model, temperature, max_tokens):
        openai.api_key = os.getenv("OPENAI_SECRET_KEY")
        self.delimiter = delimiter
        self.system_message = system_message
        self.user_message = user_message
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def create_prompt(self):
        messages =  [  
        {'role':'system', 
        'content': self.system_message},    
        {'role':'user', 
        'content': f"{self.delimiter}{self.user_message}{self.delimiter}"},  
        ]
        return messages
    
    def get_completion_from_messages(self):
        response = openai.ChatCompletion.create(
        model=self.model,
        messages=self.create_prompt(),
        temperature=self.temperature, 
        max_tokens=self.max_tokens,
        )
        return response.choices[0].message["content"]