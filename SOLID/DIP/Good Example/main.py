from notificationService import NotificationService
from emailService import EmailService
from smsService import SmsService

sms_service = SmsService()
email_service = EmailService()

ns = NotificationService(email_service)
ns.notify("Hello World")