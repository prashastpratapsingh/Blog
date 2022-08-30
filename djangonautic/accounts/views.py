from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.

def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save() #this function saves the form and returns the user to us
            login(request,user)
            return redirect('articles:list')
    else:
        form=UserCreationForm()
    return render(request,'accounts/sign_up.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            #log in
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
    
#its better practice to use POST request than GET requets while logging the user out 
#(i.e clicking nay button rather than visiting any site)

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('articles:list')
