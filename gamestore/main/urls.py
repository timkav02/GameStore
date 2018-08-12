from django.urls import path
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from .forms import AuthenticationForm
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'accounts/login/', login, {'template_name': 'login.html','authentication_form': AuthenticationForm}, name='login'),
    path(r'accounts/logout/', logout, {'next_page': '/'}, name='logout'),
]
