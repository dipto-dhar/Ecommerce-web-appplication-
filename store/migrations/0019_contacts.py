# Generated by Django 5.1 on 2024-08-25 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_alter_order_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=500)),
                ('massage', models.CharField(max_length=1500)),
            ],
        ),
    ]
