# Generated by Django 5.0.7 on 2024-10-19 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_admin', '0050_settings_button_bg_color_settings_button_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='button_bg_color',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='heading_color',
        ),
    ]
