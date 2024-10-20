# Generated by Django 5.0.6 on 2024-07-12 15:45

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_admin', '0004_alter_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='blank-sm.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(blank=True, default='', max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('image', models.ImageField(default='', upload_to='uploads/products')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ecom_admin.category')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom_admin.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom_admin.product')),
            ],
        ),
    ]
