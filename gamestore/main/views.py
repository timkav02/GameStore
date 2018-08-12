from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .forms import SignupForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return render(request, 'main/index.html', {})
