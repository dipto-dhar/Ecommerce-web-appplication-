# Generated by Django 5.0.6 on 2024-07-13 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_admin', '0008_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
