# Generated by Django 5.1 on 2024-08-26 14:39

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_admin', '0040_alter_aboutpage_page_banner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicyPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(blank=True, default='', max_length=500)),
                ('secendary_title', models.CharField(blank=True, default='', max_length=500)),
                ('page_banner', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('page_content', tinymce.models.HTMLField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='TermsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(blank=True, default='', max_length=500)),
                ('secendary_title', models.CharField(blank=True, default='', max_length=500)),
                ('page_banner', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('page_content', tinymce.models.HTMLField(blank=True, default='')),
            ],
        ),
    ]
