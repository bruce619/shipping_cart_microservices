# Generated by Django 5.1.5 on 2025-02-04 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_products_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='tite',
            new_name='title',
        ),
    ]
