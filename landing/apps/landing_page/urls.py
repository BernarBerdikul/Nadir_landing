from django.urls import path
from . import views

app_name = 'landing_page'

urlpatterns = [
    path('', views.index, name='index'),
    path('save_message/', views.save_message, name='save_message'),
    path('contact/', views.contact, name='contact'),

]
