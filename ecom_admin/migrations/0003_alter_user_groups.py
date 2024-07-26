# Generated by Django 5.0.6 on 2024-07-11 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('ecom_admin', '0002_remove_user_groups_alter_user_image_user_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]