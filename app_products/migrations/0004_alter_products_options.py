# Generated by Django 5.1.1 on 2024-09-07 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0003_products_delete_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Продукты', 'verbose_name_plural': 'Продукты'},
        ),
    ]
