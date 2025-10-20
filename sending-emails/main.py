from fastapi import FastAPI
from fastapi_mail import MessageSchema, MessageType
from pydantic import EmailStr

from .mail_client import mail_client

# fastapi dev .\main.py
app = FastAPI()

@app.post("/send")
async def send_email(recipient: EmailStr, subject: str, message_body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[recipient],
        body=message_body,
        subtype=MessageType.html
    )

    await mail_client.send_message(message)

    return {"message": "Email sent successfully!"}