from pydantic import BaseModel, Field

class RegistrationSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    password: str = Field(..., min_length=6)

class LoginSchema(BaseModel):
    username: str
    password: str
