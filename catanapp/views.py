from django.shortcuts import render
from catanapp.models import Dropable
# Create your views here.
from Catan.settings import BASE_DIR
from django.core.files.images import ImageFile

def home(request):
    ctx = {}
    return render (request,'home.html',ctx)



def play(request):
    ctx = {}
                                                                 
        
    # card1 = Dropable.objects.create(name='card1',image = f'{BASE_DIR}/static/dropables/rockhex.png') 
    
    # card1.save()

    imageObjects = Dropable.objects.all()
    imageObjectUrls = [a.image.url.split('static')[1] for a in imageObjects]

    ctx['imageObjects'] = imageObjects
    ctx['imageObjectUrls'] = imageObjectUrls
    return render (request,'play.html',ctx)