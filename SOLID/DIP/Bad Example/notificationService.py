from emailService import EmailService
from smsService import SmsService

class NotificationService:
    def __init__(self, email_service: EmailService, sms_service: SmsService):
        self.email_service = email_service
        self.sms_service = sms_service

    def send_email(self, message: str) -> None:
        self.email_service.send_email(message)

    def send_sms(self, message: str) -> None:
        self.sms_service.send_sms(message)
