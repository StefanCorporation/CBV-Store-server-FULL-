# Generated by Django 4.2.7 on 2024-02-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_options_alter_productcategory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
    ]
