from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
from typing import List

from models import User, UserAge, Feedback, FeedbackValidated

app = FastAPI(title="Контрольная работа №1")

my_user = User(name="Варя Есина", id=1)

feedbacks_db: List[dict] = []

@app.get("/", response_class=JSONResponse)
async def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

@app.get("/html", response_class=HTMLResponse)
async def get_html_page():
    return FileResponse("index.html")

@app.post("/calculate")
async def calculate(num1: float, num2: float):
    result = num1 + num2
    return {"result": result}

@app.get("/users")
async def get_user():
    return my_user

@app.post("/user")
async def check_user_adult(user: UserAge):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    feedback_dict = {"name": feedback.name, "message": feedback.message}
    feedbacks_db.append(feedback_dict)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}

@app.post("/feedback/v2")
async def create_feedback_validated(feedback: FeedbackValidated):
    feedback_dict = {"name": feedback.name, "message": feedback.message}
    feedbacks_db.append(feedback_dict)    
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}

@app.get("/feedbacks")
async def get_all_feedbacks():
    return {"feedbacks": feedbacks_db}