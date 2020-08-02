from django.forms import ModelForm
from .models import UserMessage


class UserMessageForm(ModelForm):
    class Meta:
        model = UserMessage
        fields = ('user_name', 'email', 'subject', 'message')
