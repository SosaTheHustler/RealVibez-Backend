from django.db import models
from cloudinary.models import CloudinaryField
from django.forms import ImageField

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.title