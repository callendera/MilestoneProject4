from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, default='')
    slug = models.SlugField(max_length=250, unique=True)
    description = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='images', default='')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, null=True)
    name = models.CharField(max_length=254, default='')
    brand = models.CharField(max_length=254, default='')
    slug = models.SlugField(max_length=254,  unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images', default='')

    def get_absolute_url(self):
        return reverse('products_detail', args=[self.slug])

    def __str__(self):
        return self.name