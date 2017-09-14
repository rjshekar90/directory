from django.db import models
from django.utils.text import slugify

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    #image = models.CharField(max_length = 200)
    slug  = models.SlugField(max_length = 40, blank = True)




    def save(self, *args, **kwargs):
        if not self.pk:
            slug = slugify(self.name)
        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
