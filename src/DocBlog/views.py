#from django.http import HttpResponse
from datetime import datetime 
from django.shortcuts import render

#def index(request):
#    return HttpResponse("<h1>Bienvenue</h1>")

def index (request):
     
    return render(request, "index.html", context={"date" : datetime.today() })
    
