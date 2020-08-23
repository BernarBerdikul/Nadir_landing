from django.urls import path
from . import views

app_name = 'landing_page'

urlpatterns = [
    path('', views.index, name='index'),
    path('save_and_send_message/', views.save_and_send_message, name='save_and_send_message'),
    path('contact/', views.contact, name='contact'),
    path('media/', views.media, name='media') 
]
