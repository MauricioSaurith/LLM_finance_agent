from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.agent import Agent, RunResponse
from dotenv import load_dotenv
import os


import phi
from phi.playground import Playground, serve_playground_app
phi.api_key = os.getenv("PHI_API_KEY")

load_dotenv()

## This is the Web Search Agent that can search the web for financial information
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for financial information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include source links in your answers."],
    show_tools_calls=True,
    markdown=True,

)

## Financial agent that can search the web and get financial data
finance_agent=Agent(
    name="Finance AI Agent",
    role="Financial Information Retriever",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True),
    ],
    instructions=["Use tables to display financial data"],
    show_tools_calls=True,
    markdown=True,

)

## Multi-agent system that combines web search and financial data
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    role="Multi-Agent Financial Information Retriever",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Utilice el agente de búsqueda web para encontrar información sobre la empresa y el agente financiero para encontrar información sobre las acciones.",
    "Usar tabla para mostrar los datos"],
    show_tool_calls=True,
    markdown=True
)

app = Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)