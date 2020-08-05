from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from time import sleep

@shared_task
def send_email_task(user_message_id):
    from .models import UserMessage
    send_from = settings.EMAIL_HOST_USER
    user_message = UserMessage.objects.get(id=user_message_id)
    sleep(10)
    print("HELLO BLYAT USER")
    print(user_message)
    send_mail(
        user_message.subject,
        user_message.message,
        send_from,
        ['akpayev.nadir@gmail.com',
        'bernar.berdikul@mail.ru'],
        fail_silently=False
    )
    return None
