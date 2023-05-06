from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.db.models import Q
from django.contrib import messages 

def testpage(request):
    return HttpResponse("this is connected and working !")
    

def index(request):
    context = {
        "title": "BioTech"          
    }
    return render(request, "index.html", context)


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(Q(username=username)|Q(email=username))
        auth_user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, auth_user)
            return redirect("index") 
    else:
        return render(request, "loginpage.html")
    

def user_register(request):
    if request.method == "POST":
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email address already in use!")
            return render(request, "registration.html" )    
        if pass1 != pass2:
            messages.error(request, "Password mismatch!")
            return render(request, "registration.html")
        user = User(email=email)
        user.set_password(pass2)
        user.save()
        messages.success(request, "Registration successful! Please login to continue!")
        return redirect("login")
    else:
        return render(request, "registration.html")
    




def user_logout(request):
    logout(request)
    return redirect("login")