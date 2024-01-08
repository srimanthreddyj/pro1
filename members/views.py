from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login


def loginUser(request):
     if request.method=="POST":
         username=request.POST.get('username')
         password =request.POST.get('password') 
         print(f"Username: {username}, Password: {password}")   
         user=authenticate(username=username,password=password) 
         print(f"Authenticated User: {user}")
         if user is not None:
             login(request,user)
             return redirect("/")
         else:
             return render(request,'login1.html',{})
     return render(request,'login1.html',{})
     #return render(request,'home.html',{})
     
        
def index(request):
    print('index')
    if request.user.is_anonymous:
        print("error")
        return redirect("/login_user")
    #return render(request,'login1.html',{})
    return render(request,'login1.html',{})

def logout1(request):
    logout(request)
    return redirect("/login_user")
