# Generated by Django 5.0.7 on 2024-07-31 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_admin', '0025_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]