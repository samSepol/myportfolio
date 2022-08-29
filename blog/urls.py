from django.urls import path 

from . import views

urlpatterns = [
    path('',views.Home, name='Home'),
    path('<int:blog_id>/',views.BlogDetail,name='BlogDetail'),
    path('about',views.About ,name='About'),
    path('contact',views.Contact ,name='Contact'),
]
