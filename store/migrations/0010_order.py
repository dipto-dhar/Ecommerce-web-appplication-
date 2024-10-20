# Generated by Django 5.0.7 on 2024-08-14 11:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_shippinginfo_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=20)),
                ('shipping_address', models.TextField(max_length=1000)),
                ('order_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
