from django.http import HttpResponse #alows us to send response to users
from django.shortcuts import render #allows us to render html template 

#function which is aclled when about url is done
def about(request):
    #return HttpResponse('about') 
    return render(request,'about.html')

def homepage(request):
    #return HttpResponse('home')
    return render(request,'homepage.html')