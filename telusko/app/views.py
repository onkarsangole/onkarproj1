from django.shortcuts import render
from .models import Login
# Create your views here.
def index(request):
    
    return render(request,'home.html')