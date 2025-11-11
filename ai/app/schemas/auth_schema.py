# ai/app/schemas/auth_schema.py
import re
from pydantic import BaseModel, Field, field_validator

# 간단 이메일 패턴
EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

class _EmailMixin(BaseModel):
    @field_validator("email")
    @classmethod
    def _validate_email(cls, v: str) -> str:
        if not isinstance(v, str) or not EMAIL_RE.match(v):
            raise ValueError("Invalid email format")
        return v.strip().lower()

class RegisterRequest(_EmailMixin):
    email: str
    name: str = Field(min_length=1, max_length=64)
    password: str = Field(min_length=8, max_length=128)

class RegisterResponse(_EmailMixin):
    user_id: int
    email: str
    name: str
    created_at: str

class LoginRequest(_EmailMixin):
    email: str
    name: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int = 7200

class UserInfo(_EmailMixin):
    user_id: int
    email: str
    name: str
    created_at: str
