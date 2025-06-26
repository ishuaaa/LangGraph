from typing import TypedDict,List
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph,START,END
from dotenv import load_dotenv

load_dotenv()

class Agentstate(TypedDict):
    message:List[HumanMessage]

llm= ChatOpenAI(model="gpt-4o")


def process(state:Agentstate)->Agentstate:
    response=llm.invoke(state["message"])
    print(f"\nAI: {response.content}")
    return state

graph=StateGraph(Agentstate)
graph.add_node("Process_node",process)
graph.add_edge(START,"Process_node")
graph.add_edge("Process_node",END)
agent=graph.compile()

user_input=input("ENTER:")
agent.invoke({"message":[HumanMessage(content=user_input)]})