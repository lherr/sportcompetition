from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls.base import reverse

# Create your views here.

def main(request):
    return render(request, 'sportcompetition/main.html', {})

def login_view(request):
    login_form = AuthenticationForm()
    if request.method == "POST":
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
    return render(request, 'sportcompetition/login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect(reverse('sportcompetition:main'))