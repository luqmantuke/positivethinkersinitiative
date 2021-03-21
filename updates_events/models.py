from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from positivethinkers.utils import unique_slug_generator
from django.utils import timezone


class Updates(models.Model):
    name = models.CharField(max_length=1000)
    time = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='projects', null=True)
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('updates_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender = Updates)


