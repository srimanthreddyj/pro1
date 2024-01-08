from urllib import request
from django.shortcuts import render
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        emale=request.POST.get('emale')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,emale=emale,phone=phone,desc=desc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')


def services(request):
    return render(request,'services.html')