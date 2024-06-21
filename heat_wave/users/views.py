from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse,   HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate , login, logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            user = User.objects.filter(email=email)
            
            if user.exists():
                messages.info(request, 'User with this email already exists')
                return redirect("/users/signup")
            
            user = User.objects.create_user(username=email)
            
            user.set_password(password)
            user.save()
            
            messages.info(request, 'User created successfully')
            return render('/users/login.html')
    template = loader.get_template('users/signup.html')
    context = {}
    return HttpResponse(template.render(context,request))


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
     
        if not User.objects.filter(email=email):
            messages.info(request, 'User with this email does not exist')
            return redirect('/users/login')    
        user = authenticate(request,email=email, password = password)
        
        if user is None:
            messages.info(request, 'invalid password')
            return redirect('/users/login')
        
        login(request, user)
        messages.info(request,'login successful')
        
        return redirect('/oj/homepage')
    
    return render(request, "users/login.html")


def logout_user(request):
    logout(request)
    messages.info(request, 'logout successful')
    return render(request ,'users/login.html')
 




    
        
