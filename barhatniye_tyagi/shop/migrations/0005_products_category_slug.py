# Generated by Django 4.1.7 on 2023-04-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category_slug',
            field=models.SlugField(null=True),
        ),
    ]
