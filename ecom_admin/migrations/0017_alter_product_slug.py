# Generated by Django 5.0.6 on 2024-07-13 17:46

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_admin', '0016_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=500, null=True, populate_from='name', unique=True),
        ),
    ]