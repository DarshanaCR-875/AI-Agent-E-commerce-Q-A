import sqlite3
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.base import SQLDatabaseToolkit, create_sql_agent
from langchain.agents.agent_types import AgentType

# Step 1: Connect to your database
db = SQLDatabase.from_uri("sqlite:///ecommerce.db")

# Step 2: Load your LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key="MY_API_KEY")

# Step 3: Create toolkit from db
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Step 4: Create agent
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# Step 5: Run question through agent
def ask_question(user_query):
    try:
        return agent_executor.run(user_query)
    except Exception as e:
        return f"[ERROR] {str(e)}"




    




    
