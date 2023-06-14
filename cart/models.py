from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Catagory(models.Model):
    catagory_name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=300, blank= True)
    img = models.ImageField(upload_to = 'projectImg', blank= True)
    
    class Meta:
        verbose_name = 'catagory'
        verbose_name_plural = 'catagories'
        
        
    def get_url(self):
        return reverse('products_by_cata', args=[self.slug])
        
    def __str__(self):
        return self.catagory_name
    
        