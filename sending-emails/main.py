from fastapi import FastAPI
from fastapi_mail import MessageSchema, MessageType

from .mail_client import mail_client
from .schema import EmailSchema

# fastapi dev .\main.py
app = FastAPI()

@app.post("/send")
async def send_email(model: EmailSchema):
    message = MessageSchema(
        subject="Confirm your account",
        recipients=model.recipients,
        template_body={
            "username": model.username,
            "confirm_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        },
        subtype=MessageType.html
    )

    await mail_client.send_message(message, template_name="confirm.html")

    return {"message": "Email sent successfully!"}