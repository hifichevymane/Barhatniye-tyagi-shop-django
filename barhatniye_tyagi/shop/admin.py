from django.contrib import admin
from shop.models import Product, Category, Brand
from django.utils.text import slugify

# Register your models here.

# Products admin panel
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

    # Automatic generating a product slug
    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)


# Brand admin panel
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

    # Automatic generating a brand slug
    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)


# Registrating all models
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand, BrandAdmin)
