from django.db import models


class UserMessage(models.Model):
    user_name = models.CharField(max_length=50, verbose_name='имя')
    email = models.EmailField(null=True, blank=True, verbose_name='эл. адрес')
    subject = models.CharField(max_length=100, verbose_name='тема вопроса')
    message = models.TextField(verbose_name='текст')

    def __str__(self):
        return f'{self.user_name} - {self.email} - {self.subject}'

    class Meta:
        verbose_name = 'Сообщение от пользователя'
        verbose_name_plural = 'Сообщения пользователей'
