# Generated by Django 5.0.7 on 2024-07-31 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_admin', '0024_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=500),
        ),
    ]