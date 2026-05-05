from django.contrib.auth.models import User
from django.shortcuts import render,redirect


def user_register(request):
    if request.method=="POST":
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POSt.get("password")

        if User.objects.filter(email=email).exists():
            return redirect('register')
    return render(request,'account/register.html')

def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POSt.get("password")


    return render(request,'account/accounts.html')



