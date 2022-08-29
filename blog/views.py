from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.

def Home(request):
    blogs= Blog.objects.all()
    return render(request,'blogs/home.html',{'blogs':blogs})

def BlogDetail(request,blog_id):
    blog_details=get_object_or_404(Blog,pk=blog_id)
    print(blog_details)
    return render(request,'blogs/detail.html',{'blog_details':blog_details})

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
    return render(request,'blogs/contact.html')