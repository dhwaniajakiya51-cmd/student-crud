import re
from pydantic import BaseModel, Field, field_validator


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: str
    course: str = Field(..., min_length=2, max_length=100)
    semester: int = Field(..., ge=1, le=12)

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        value = value.strip()

        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", value):
            raise ValueError("Invalid email address")

        return value


class StudentUpdate(StudentCreate):
    pass


class StudentResponse(StudentCreate):
    id: int