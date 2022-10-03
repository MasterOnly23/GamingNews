from django.shortcuts import render
from requests import request
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

#@login_required
def home(request):
    return render(request, 'home.html')














def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)

            if user is not None:
                login(request, user)
                return render(request, 'home.html')


            else:
                return render(request, 'login.html', {'form':form})
        
        else:
            return render(request, 'login.html', {'form':form})

    form = AuthenticationForm()
    return render(request, 'login.html')
