# create a fast api app which calls get_answer() from cahatbot.py

from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_answer
from recomend import get_recommeded
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# origins = [
#   "http://localhost:3000",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str


class Desc(BaseModel):
    desc: str


@app.post("/answer")
def answer_question(question: Question):
    answer = get_answer(question.question)
    return {"answer": answer}


@app.post("/recommeded")
def recommeded_desc(desc: Desc):
    recommeded = get_recommeded(desc.desc)
    return {"recommeded": recommeded}

# run the app


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)