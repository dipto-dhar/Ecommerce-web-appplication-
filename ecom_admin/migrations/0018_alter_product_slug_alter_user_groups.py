# Generated by Django 5.0.6 on 2024-07-18 18:26

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('ecom_admin', '0017_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]
