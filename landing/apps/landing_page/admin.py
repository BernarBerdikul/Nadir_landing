from django.contrib import admin
from .models import UserMessage


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'subject', 'message')
    list_display_links = ('user_name', 'email')
    search_fields = ('user_name', 'email',)
