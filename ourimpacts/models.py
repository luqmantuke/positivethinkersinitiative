from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from positivethinkers.utils import unique_slug_generator

# Create your models here.

category_list = (('Videos', 'Videos'), ('Stories', 'Stories'), ('Activities', 'Activities'))

class OurImpacts(models.Model):
    name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='our_impacts', null=True)
    date = models.DateTimeField(auto_now_add=True)
    description = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=300, choices=category_list, null=True)
    slug = models.SlugField(null=True, blank=True)


    def __str__(self):
        return self.name


