from django.shortcuts import render

# Create your views here.


def home(request):
    ctx = {}
    return render (request,'home.html',ctx)



def play(request):
    ctx = {}
    return render (request,'play.html',ctx)