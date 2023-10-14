#

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=300, unique=True)
    description = RichTextField()
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Size(models.Model):
    size = models.CharField(max_length=300)

    def __str__(self):
        return self.size


class Product(models.Model):
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name='collection')
    name = models.CharField(max_length=300)
    prize = models.IntegerField()
    description = models.TextField()
    size = models.ManyToManyField(Size, blank=True)
    # length =

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.image.name
