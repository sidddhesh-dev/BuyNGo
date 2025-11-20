from django.shortcuts import render

def accounts(request):
    return render(request,'account/accounts.html')
