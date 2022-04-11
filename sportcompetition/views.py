from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls.base import reverse
from .forms import LoginForm

# Create your views here.

def main(request):
    return render(request, 'sportcompetition/main.html', {})

def login_view(request):
    if request.user.is_authenticated:
        return render(request, 'sportcompetition:member')
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('sportcompetition:member'))
    return render(request, 'sportcompetition/login.html', {'login_form': login_form})



@login_required
def member_view(request):
    return render(request, 'sportcompetition/member.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('sportcompetition:main'))
