import collections
import sys
import os
from typing import Optional
import logging
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Check Python version and import appropriate MutableSet and MutableMapping
if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    from collections.abc import MutableSet
    collections.MutableSet = collections.abc.MutableSet
    collections.MutableMapping = collections.abc.MutableMapping
else:
    from collections import MutableSet, MutableMapping

# Set OpenAI API environment variables
os.environ["OPENAI_API_TYPE"] = "openai"
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Define a Pydantic model for response analysis
class ResponseAnalysis(BaseModel):
    """Result topic query"""
    python_code: Optional[str] = Field(..., description="Improved python code")

# Class to improve a given model
class ModelImprove:
    def __init__(self, text):
        self.text = text
        logging.info("ModelImprove instance created with text: %s", text)

    def model_first_answer(self):
        """Generate the first improved model answer"""
        try:
            prompt_eng = """you must comment, add logs, try and exception clauses in this next script {user_input}
            and return the python code improved"""

            template = prompt_eng
            prompt = ChatPromptTemplate.from_messages([
                ("system", template,),
                ("human", "Question: {question}")
            ])
            llm = ChatOpenAI(model="gpt-4o", temperature=0.15)
            chain = prompt | llm.with_structured_output(schema=ResponseAnalysis)
            model_improve_answer = chain.invoke({"question": template, "user_input": self.text})
            logging.info("Model first answer generated.")

            return model_improve_answer.python_code
        except Exception as e:
            logging.error("Error in model_first_answer: %s", e)
            return None

    def model_improve_response_reflexor(self):
        """Improve the response reflexively"""
        try:
            template = """
                You must improve this code, add loggings, comments and improve this script
                The code must be executable, and meet the client's expectations, 
                check that the code is executable and goes according to specified requirements
                {python_script}
                """

            apikey = os.getenv("OPENAI_API_KEY")
            prompt = ChatPromptTemplate.from_messages([
                ("system", template,),
                ("human", "user_input: {user_input}")
            ])
            llm = ChatOpenAI(openai_api_key=apikey, model="gpt-4o", temperature=0.15)
            chain = prompt | llm.with_structured_output(schema=ResponseAnalysis)
            model_improve_answer = chain.invoke({"question": template, "user_input": self.text})
            logging.info("Analysis improvement response generated.")
            return model_improve_answer.python_code
        except Exception as e:
            logging.error("Error in model_improve_response_reflexor: %s", e)
            return None

# Function to write improved code to a file
def write_code(path: str, code: str):
    """Write the improved code to a specified file path"""
    try:
        with open(path, "w") as script:
            script.write(code)
            logging.info("Code successfully written to %s", path)
            print("Code improved")
    except Exception as e:
        logging.error("Failed to write code to %s: %s", path, e)