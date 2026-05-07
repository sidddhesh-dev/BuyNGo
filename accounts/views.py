from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate


def user_register(request):
    if request.method=="POST":
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POSt.get("password")

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
        password=request.POSt.get("password")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"user login successful")
            return redirect('home')

    

    


    return render(request,'account/accounts.html')



