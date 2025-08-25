from langchain.llms import OpenAI
from langchain.chains import ConversationChain

class LangAgent:
    def __init__(self, api_key: str):
        self.llm = OpenAI(api_key=api_key)
        self.chain = ConversationChain(llm=self.llm)

    def run(self, prompt: str) -> str:
        return self.chain.run(prompt)
