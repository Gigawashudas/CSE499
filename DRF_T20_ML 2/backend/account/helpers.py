from django.core.mail import send_mail
from django.conf import settings


def send_forgot_password_mail(email, token):
    subject = 'Your reset password link'
    message = f'Hi, click on the link to reset your password http://127.0.0.1:8000/account/change-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=email_from, recipient_list=recipient_list)
    return True
