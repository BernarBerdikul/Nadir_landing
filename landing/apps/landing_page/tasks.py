from celery import shared_task
from django.core.mail import send_mail
from time import sleep
from .models import UserMessage


@shared_task
def send_email_task(user_message_id, email):
    send_from = email
    print('test2')
    user_message = UserMessage.objects.get(id=user_message_id)
    sleep(10)
    send_mail(
        user_message.subject,
        user_message.message,
        send_from,
        ['bernar.berdikul@mail.ru'],
        fail_silently=False
    )
    return None
