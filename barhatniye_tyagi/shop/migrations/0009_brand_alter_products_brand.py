# Generated by Django 4.2.1 on 2023-05-21 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_category_remove_products_category_slug_products_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.brand'),
        ),
    ]
