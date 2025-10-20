from pydantic import BaseModel, EmailStr


class EmailSchema(BaseModel):
    recipients: list[EmailStr]
    username: str