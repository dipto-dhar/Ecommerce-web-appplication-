# Generated by Django 5.0.6 on 2024-07-13 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_admin', '0009_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=100),
        ),
    ]
