from django.shortcuts import render

def homepage(request):
    return render(request, 'home/home.html')

def developer(request):
    return render(request,'home/developer.html')

def about(request):
    return render(request, 'home/about.html')

def features(request):
    return render(request, 'home/features.html')

def developer(request):
    return render(request, 'home/developer.html')
