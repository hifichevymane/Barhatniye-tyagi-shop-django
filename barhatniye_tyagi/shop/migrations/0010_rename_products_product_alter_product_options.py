# Generated by Django 4.2.1 on 2023-05-21 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_brand_alter_products_brand'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
