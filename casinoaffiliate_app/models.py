from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Casino(models.Model): 
    name = models.CharField(max_length=200) 
    slug = models.SlugField(unique=True)
    small_description = models.TextField(null=True, blank=True)
    description = RichTextField()
    url = models.URLField()
    img = models.ImageField(upload_to='') 
  
    def __str__(self): 
        return self.name

class AdminReview(models.Model):
    casino = models.ForeignKey('Casino', on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, blank=True)
    guarantee_support = models.BooleanField(default=False)
    point = models.FloatField()

class Bonus(models.Model):
    casino = models.ForeignKey('Casino', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    promo_code = models.CharField(max_length=50, blank=True, null=True, default='-')
    description = models.TextField(blank=True, null=True)

    def __str__(self): 
        return self.casino.name + ' - ' + self.title