from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        email= request.POST['email']
        password=request.POST['password']
       
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username already exists")
            return redirect('authen:register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already used. Please login")
            return redirect('authen:register')

        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            print("usercreated") 
    
            return redirect('authen:login')
    else:
        return render(request,'register.html')
     

def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
           
            return redirect('papp:index')
        else:
            messages.info(request,"Invalid Login")
            return redirect ('authen:login')
    else:
        # Handle GET request by rendering the login form
        return render(request, 'login.html')  # Make sure you have 'login.html' template

def logout(request):
    auth.logout(request)

    return redirect ('papp:index')