from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

# Categories model
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    # Changing default names for Category model
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    # Making URL path for model object for slug
    def get_absolute_url(self):
        return reverse("card", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.name} - {self.slug}"


# Brand model
class Brand(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    # Automatic generating slug in slug field
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.slug}'
    

# Products model
class Product(models.Model):
    name = models.CharField(max_length=128, blank=False)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    price = models.FloatField(blank=False)
    short_description = models.CharField(max_length=128, default="НЕТ ОПИСАНИЯ")
    description = models.TextField(blank=False)
    image = models.ImageField(blank=False ,default=None, upload_to='images/')

    # Changing default names for product model
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"name: {self.name} | category: {self.category} | brand: {self.brand}"
