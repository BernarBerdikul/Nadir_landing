from django.http import HttpResponseRedirect, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import UserMessageForm
from django.urls import reverse
from .tasks import send_email_task

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

@method_decorator(csrf_exempt)
def save_message(request):
    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            user_message = form.save()
            print("id blyat:" + str(user_message.id))
            send_email_task.delay(user_message.id)
            print("Zdes problema blyat")
            return HttpResponseRedirect(reverse('landing_page:index'))
        else:
            return HttpResponse('<h1>Форма не заполнена полностью</h1>')

