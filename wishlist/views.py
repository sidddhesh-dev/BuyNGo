from django.shortcuts import render

def wishlist_data(request):
    return render(request,'wishlist/wishlist.html')
