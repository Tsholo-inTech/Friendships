from django.http import HttpResponse
from django.shortcuts import render


def portfolio(request):
    #return HttpResponse("We're up all night to get lucky, with these college friends")
    return render(request, 'portfolio.html')


def explore(request):
    #return HttpResponse("Find Your Perfect Friends")    
    return render(request, 'explore.html')

def platform(request):
    #return HttpResponse("Find Your Perfect Friends")    
    return render(request, 'platform.html')

