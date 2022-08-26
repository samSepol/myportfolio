from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog
# Create your views here.

def Home(request):
    blogs= Blog.objects.all()
    return render(request,'blogs/home.html',{'blogs':blogs})

def About(request):
    content={
        'author':"Samarth Parale",
        'Framework':{
            'python':'django',
            'javascript':'vue',
            'database':'MongoDB',
        }
    }
    return render(request,'blogs/about.html',content)

def Contact(request):
    return render(request,'blog/contact.html')