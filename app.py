from fastapi import FastAPI
from pydantic import BaseModel
from query_engine import ask_question

app = FastAPI()

class Question(BaseModel):
    query: str

@app.post("/ask")
def ask(question: Question):
    response = ask_question(question.query)
    return {"response": response}
