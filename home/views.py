from django.shortcuts import render

def homepage(request):
    return render(request, 'home/home.html')

def developer(request):
    return render(request,'home/developer.html')

def about(request):
    return render(request, 'home/about.html')

def categories(request):
    return render(request, 'home/categories.html')

def developer(request):
    return render(request, 'home/developer.html')
