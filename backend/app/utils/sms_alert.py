from twilio.rest import Client
import os

client = Client(
    os.getenv("TWILIO_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)

def send_sms(message: str):
    client.messages.create(
        body=message,
        from_=os.getenv("TWILIO_PHONE"),
        to=os.getenv("EMERGENCY_PHONE")
    )