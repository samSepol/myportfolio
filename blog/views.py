from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def Home(request):
    return render(request,'home.html')

def About(request):
    content={
        'author':"Samarth Parale",
        'Framework':{
            'python':'django',
            'javascript':'vue',
            'database':'MongoDB',
        }
    }
    return render(request,'about.html',content)

def Contact(request):
    return render(request,'contact.html')