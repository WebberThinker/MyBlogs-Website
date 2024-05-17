from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='static/images')
    snippet = models.CharField(max_length=250)
    post_date = models.DateField(auto_now_add=True)
    body = RichTextField()

    def __str__(self):
        return self.title
        
class Contact(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.first_name
    
    def get_absolute_url(self):
        return reverse("home")
    