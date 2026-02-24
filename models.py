from pydantic import BaseModel, Field, field_validator

# Задание 1.4: Модель User с id и name
class User(BaseModel):
    name: str
    id: int

# Задание 1.5: Модель UserAge для проверки возраста
class UserAge(BaseModel):
    name: str
    age: int

# Задание 2.1: Модель Feedback (базовая)
class Feedback(BaseModel):
    name: str
    message: str

# Задание 2.2: Модель Feedback с валидацией
class FeedbackValidated(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Имя от 2 до 50 символов")
    message: str = Field(..., min_length=10, max_length=500, description="Сообщение от 10 до 500 символов")
    
    # Кастомная валидация для запрещенных слов
    @field_validator('message')
    @classmethod
    def check_forbidden_words(cls, v: str) -> str:
        forbidden_words = ['крингк', 'рофл', 'вайб']
        # Приводим к нижнему регистру для проверки
        v_lower = v.lower()
        for word in forbidden_words:
            if word in v_lower:
                raise ValueError(f'Использование недопустимых слов: "{word}"')
        return v
