from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
from typing import List

# Импортируем модели из models.py
from models import User, UserAge, Feedback, FeedbackValidated

# Задание 1.1: Создание приложения FastAPI
app = FastAPI(title="Контрольная работа №1")

# Задание 1.4: Создаем экземпляр класса User с твоими данными
my_user = User(name="Варя Есина", id=1)

# Задание 2.1 и 2.2: Хранилище для отзывов
feedbacks_db: List[dict] = []

# ==================== Задание 1.1 ====================
@app.get("/", response_class=JSONResponse)
async def root():
    """
    Корневой маршрут, возвращает JSON с приветствием
    """
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

# ==================== Задание 1.2 ====================
@app.get("/html", response_class=HTMLResponse)
async def get_html_page():
    """
    Возвращает HTML-страницу из файла index.html
    """
    return FileResponse("index.html")

# ==================== Задание 1.3 ====================
@app.post("/calculate")
async def calculate(num1: float, num2: float):
    """
    Принимает два числа в query параметрах и возвращает их сумму
    Пример: /calculate?num1=5&num2=10
    """
    result = num1 + num2
    return {"result": result}

# ==================== Задание 1.4 ====================
@app.get("/users")
async def get_user():
    """
    Возвращает данные пользователя из модели User
    """
    return my_user

# ==================== Задание 1.5 ====================
@app.post("/user")
async def check_user_adult(user: UserAge):
    """
    Принимает JSON с пользователем (name, age) и возвращает
    те же данные с полем is_adult
    """
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

# ==================== Задание 2.1 ====================
@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    """
    Принимает JSON с отзывом (name, message) и сохраняет его в список
    """
    # Сохраняем отзыв в базу данных (список)
    feedback_dict = {"name": feedback.name, "message": feedback.message}
    feedbacks_db.append(feedback_dict)
    
    return {"message": f"Feedback received. Thank you, {feedback.name}."}

# ==================== Задание 2.2 ====================
@app.post("/feedback/v2")
async def create_feedback_validated(feedback: FeedbackValidated):
    """
    Принимает JSON с отзывом (name, message) с валидацией:
    - name: от 2 до 50 символов
    - message: от 10 до 500 символов, без запрещенных слов
    """
    # Сохраняем отзыв
    feedback_dict = {"name": feedback.name, "message": feedback.message}
    feedbacks_db.append(feedback_dict)
    
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}

# ==================== Дополнительный маршрут для проверки ====================
@app.get("/feedbacks")
async def get_all_feedbacks():
    """
    Возвращает все сохраненные отзывы (для проверки)
    """
    return {"feedbacks": feedbacks_db}

# Для запуска: uvicorn app:app --reload
