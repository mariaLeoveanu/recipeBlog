from django.db import models
from django.contrib.auth.models import User
from django import forms
from PIL import Image

# Create your models here.
from django.urls import reverse
import datetime
from django.utils import timezone

recipe_types = [
    ("Appetizer", "Appetizer"),
    ("Main-Course", "Main-Course"),
    ("Garnish", "Garnish"),
    ("Desert", "Desert"),
    ("Drink", "Drink")
]
default_duration = datetime.timedelta(minutes=45)


class Recipe(models.Model):
    name = models.CharField(max_length=150)
    preparation = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=50, choices=recipe_types, default='Main-Course')
    image = models.ImageField(default='default_recipe.jpg', upload_to='recipe_imgs')
    ingredients = models.TextField()
    duration = models.CharField(default='0 hours, 0 minutes', max_length=50)
    overview = models.TextField(default='No description.')

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
