from langchain_core.pydantic_v1 import BaseModel, Field
import collections
import sys
import os
if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    from collections.abc import MutableSet

    collections.MutableSet = collections.abc.MutableSet
    collections.MutableMapping = collections.abc.MutableMapping
else:
    from collections import MutableSet, MutableMapping
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from typing import Optional
from dotenv import load_dotenv
import logging

load_dotenv()

os.environ["OPENAI_API_TYPE"] = "openai"
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

class Response_analysis(BaseModel):
    """Result topic query"""
    python_code: Optional[str] = Field(..., description="improved python code")

class model_improve:
    def __init__(self, text, user_suggestions=None):
        self.text = text
        self.user_suggestions = user_suggestions  # Optional user input for extra improvements

    def model_first_answer(self):
        if self.user_suggestions:
            prompt_eng = """You must comment, add logs, and try-exception clauses to this script:
            {user_input}. Additionally, please incorporate these user suggestions: {user_suggestions}.
            Make redundant code into functions with best practices and return the improved python code."""
        else:
            prompt_eng = """You must comment, add logs, try-exception clauses to this script: {user_input}.
            Make redundant code into functions with best practices and return the python code improved."""

        template = prompt_eng
        prompt = ChatPromptTemplate.from_messages([("system", template,), ("human", "Question: {question}"), ])
        llm = ChatOpenAI(model="gpt-4o", temperature=0.15)
        chain = prompt | llm.with_structured_output(schema=Response_analysis)

        model_improve_answer = chain.invoke({
            "question": template,
            "user_input": self.text,
            "user_suggestions": self.user_suggestions if self.user_suggestions else ""
        })

        logging.info("Model first answer generated.")
        return model_improve_answer.python_code

    def model_improve_response_reflexor(self):
        template = """
        You must improve this Python script by:
        - Adding comments, logs, and try-exception clauses
        - Refactoring redundant code into functions following best practices
        - Ensuring the code is compliant with PEP8 standards
        The code must be executable and meet the client's expectations.
        Please return the improved Python code."""

        apikey = api_key
        prompt = ChatPromptTemplate.from_messages([("system", template,), ("human", "user_input: {user_input}")])
        llm = ChatOpenAI(openai_api_key=apikey, model="gpt-4o", temperature=0.15)
        chain = prompt | llm.with_structured_output(schema=Response_analysis)
        model_improve_answer = chain.invoke({"question": template, "user_input": self.text,})
        logging.info("Analysis improvement response generated.")
        return (model_improve_answer.python_code)

def write_code(path:str, code:str):
    with open(path, "wb") as script:
        script.write(code)
        return print("code improved")
