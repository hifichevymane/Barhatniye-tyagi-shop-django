# Generated by Django 4.1.7 on 2023-04-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_products_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category_slug',
            field=models.SlugField(choices=[('Обувь', 'shoes'), ('Куртки', 'jackets'), ('Рубашки', 'shirts')], null=True),
        ),
    ]