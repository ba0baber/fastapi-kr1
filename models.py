from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    name: str
    id: int

class UserAge(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str
    message: str

class FeedbackValidated(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Имя от 2 до 50 символов")
    message: str = Field(..., min_length=10, max_length=500, description="Сообщение от 10 до 500 символов")
    
    @field_validator('message')
    @classmethod
    def check_forbidden_words(cls, v: str) -> str:
        forbidden_words = ['крингк', 'рофл', 'вайб']
        v_lower = v.lower()
        for word in forbidden_words:
            if word in v_lower:
                raise ValueError(f'Использование недопустимых слов: "{word}"')
        return v
