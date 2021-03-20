from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.utils import timezone
from positivethinkers.utils import unique_slug_generator


class Projects(models.Model):
    name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='projects', null=True)
    description = RichTextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('projects_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender = Projects)


