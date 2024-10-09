from abc import ABC, abstractmethod
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI
from llama_index.agent.openai import OpenAIAgent

class BaseAgent(ABC):
    def __init__(self, state):
        self.state = state
        self.tools = self.get_tools()
        self.agent = OpenAIAgent.from_tools(
            self.tools,
            llm=OpenAI(model="gpt-4o"),
            system_prompt=self.get_system_prompt(),
        )

    @abstractmethod
    def get_tools(self):
        pass

    @abstractmethod
    def get_system_prompt(self):
        pass

    def run(self, input_text, chat_history):
        return self.agent.chat(input_text, chat_history=chat_history)