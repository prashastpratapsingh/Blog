from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    articles= Article.objects.all().order_by('date') #grabs all data from Article table (class in models.py represent a table in the database)
    return render(request,'articles/article_list.html',{'articles':articles}) # when we render our page( i.e article_list.html) we want to send the data retrieved in above line

def article_detail(request,slug):
    #return HttpResponse(slug)
    article=Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method=='POST':
        #if the method is post then we want to take the data that we retrieved from the 
        #create article form
        form=forms.CreateArticle(request.POST,request.FILES)
        #request.POST is validating the data that we recieved from our post (note that files(we gave an option to uplaod pics in create article form) do not come alongwith post data, we have to mention it separately)
        #the above function is validating that data
        if form.is_valid():
            #save articel to database
            instance=form.save(commit=False) #form.save anything to database, form.save returns instance of the form or the aricle
            #commit=false says do not save immediatly, we may tinker around with the instance( like we do now to set the user name automatically and then we will save the instance in the database)
            instance.author=request.user
            instance.save()
            return redirect('articles:list')
        
    else:
        form=forms.CreateArticle()
    return render(request,'articles/article_create.html',{'form':form})