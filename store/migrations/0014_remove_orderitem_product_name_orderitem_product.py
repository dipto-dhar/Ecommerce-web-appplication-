# Generated by Django 5.0.7 on 2024-08-14 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_admin', '0028_delete_order'),
        ('store', '0013_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product_name',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom_admin.product'),
        ),
    ]
