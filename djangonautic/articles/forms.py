#all form for this app are here
from django import forms
from . import models

#a form is a class in python
class CreateArticle(forms.ModelForm):
    class Meta:
        model=models.Article #which model we are using in the form
        fields=['title','body','slug','thumb'] 
