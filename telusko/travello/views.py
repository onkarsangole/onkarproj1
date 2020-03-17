from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    d1 = Destination()
    d1.name = "GOA"
    d1.price = 1000
    d1.desc = "It is good place for bachelors"
    d1.img = "destination_1.jpg"
    d1.offer = False


    d2 = Destination()
    d2.name = "Kerala"
    d2.desc = "Its is Best place for Enjoyment and to see Green Enviroment"
    d2.img = "destination_2.jpg"
    d2.price =700
    d2.offer = True

    d3 = Destination()
    d3.name = "Mumbai"
    d3.desc = "Good to see Taj Hotel and International Airport"
    d3.img = "destination_3.jpg"
    d3.price =750
    d3.offer = False


    dests = [d1,d2,d3]
    return render(request,'index.html', {'dests':dests})


def register(request):
    return render(request,'register.html')