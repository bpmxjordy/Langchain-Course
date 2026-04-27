from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()



def main():
    print("Hello from langchain-course!")
    information = ["Elon Musk"]

    facts = []

    for i in information:

        summary_template = f"""
        Given the following person: {i} return:
        1. Date of birth.
        2. Two interesting facts about the person.
        3. Their latest accomplishment.
        """

        summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

        llm = ChatOpenAI(model="gpt-4o", temperature=0)

        chain = summary_prompt_template | llm

        response = chain.invoke(input={"information": i})

        facts.append([response.content])

    for i in facts:
        print(i)
if __name__ == "__main__":
    main()
