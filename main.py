import os
from dotenv import load_dotenv
from langchain.tools import tool, Tool
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent, AgentType
from langchain.agents import AgentExecutor
from langchain_google_genai import ChatGoogleGenerativeAI

#loading the environment variable from .env
load_dotenv()

# Load API keys
serpapi_key = os.environ.get('SERPAPI_API_KEY')
google_api_key = os.environ.get('GOOGLE_API_KEY')


# Custom tool
@tool
def return_text_len(text: str) -> int:
    """Returns the length of the input text."""
    return len(text)

# SerpAPI search tool
search_tool = Tool(
    name="Amazon Search",
    func=SerpAPIWrapper(serpapi_api_key=serpapi_key).run,
    description="Use this tool to search current events and general facts from the web."
)

# Language model (free and local via Ollama)
#llm = ChatOllama(model="gemma:2b", temperature=0)
# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
# llm = ChatOllama(model="mistral", temperature=0)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# Create the agent
agent = initialize_agent(
    tools=[search_tool, return_text_len],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Wrap with executor to handle parsing errors
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent.agent,
    tools=[search_tool, return_text_len],
    verbose=True,
    handle_parsing_errors=True,
    return_intermediate_steps=True
)

# Call inputs
response1 = agent_executor.invoke({"input": "is there any laptop under 70k with gpu to fine tune LLM's locally if so provide me a link to buy that please?"})

response2 = agent_executor.invoke({"input": "How many letters are in the word 'Amazon'?"})

# Print
if __name__ == "__main__":
    print("Hi hari...you here again...")
    print("Response 1 Output:", response1["output"])
    print("Response 2 Output:", response2["output"])
