from unicodedata import name
from django.urls import path
from . import views
import sportcompetition

app_name = 'sportcompetition'
urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

