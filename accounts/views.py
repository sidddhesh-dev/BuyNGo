from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from orders.views import checkout

User = get_user_model()

def user_register(request):
    if request.method=="POST":
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")

        if User.objects.filter(email=email).exists():
            messages.warning(request,"this email alredy exsists try to login")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.warning(request,"username alerady exists")
            return redirect('register')
        
        User.objects.create_user(
            email=email,
            username=username,
            password=password
        )
        messages.success(request,"user successfully registred")
        return redirect('login')
    return render(request,'account/register.html')

def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"user login successful")
            return redirect('home')

    return render(request,'account/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
def account_user(request):
    return render(request,'account/account.html')





