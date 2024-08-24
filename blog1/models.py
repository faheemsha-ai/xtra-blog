from django.db import models

class Post(models.Model):
    item = models.CharField(max_length=100,blank=False)
    image = models.ImageField(upload_to='images/', blank=True)
    content = models.TextField(max_length=500,blank=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.item
    
class Login(models.Model):
    username = models.CharField(max_length=400,blank=False)
    password = models.CharField(max_length=500,blank=False)

    def __str__(self):
        return self.username