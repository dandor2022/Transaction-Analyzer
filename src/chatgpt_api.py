import time
from openai import OpenAI
from typing import List, Dict


class ChatGPTRequest:
    def __init__(self, chat_history: List, api_key: str, model: str = "gpt-3.5-turbo"):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.chat_history = chat_history

    def get_single_completion(self, prompt: str, temperature: float = 0) -> str:
        messages = [{"role": "user", "content": prompt}]
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
        )

        return completion.choices[0].message.content

    def get_multi_completion(self, messages: List[dict], temperature: float = 0) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
        )
        return completion.choices[0].message.content

    def append_to_history(self, role: str, content: str) -> None:
        self.chat_history.append({"role": f"{role}", "content": f"{content}"})

    def initiate(self, initial_prompt: Dict) -> None:
        for role, content in initial_prompt.items():
            self.append_to_history(role, content)

    def send_gpt_request(self) -> str:
        gpt_extraction = self.get_multi_completion(self.chat_history)
        self.append_to_history("assistant", gpt_extraction)
        return gpt_extraction

    # For debugging purposes
    def print_chat_history(self):
        for prompt in self.chat_history:
            print(prompt)
