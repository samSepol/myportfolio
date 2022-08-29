from pyexpat import model
from django.db import models

# Create your models here.

class Blog(models.Model):

     #  Blogs models fields

    title=models.CharField(max_length=255)
    logo = models.ImageField(upload_to='blog_images/')
    description = models.TextField()
    author = models.CharField(max_length=255)
    date = models.DateField()
    time  = models.TimeField()
    
    def __str__(self):
        return f'{self.title}  |  {self.author}   | {self.date}  | {self.time}'

    def summary(self):
        return f'{self.description[:100]}...'