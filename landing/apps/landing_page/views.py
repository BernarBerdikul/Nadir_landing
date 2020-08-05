from django.http import HttpResponseRedirect, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import UserMessageForm
from django.urls import reverse


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'landing/contact.html')

@method_decorator(csrf_exempt)
def save_message(request):
    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('landing_page:index'))
        else:
            return HttpResponse('<h1>Форма не заполнена полностью</h1>')
