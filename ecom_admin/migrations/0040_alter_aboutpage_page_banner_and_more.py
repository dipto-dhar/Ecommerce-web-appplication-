# Generated by Django 5.1 on 2024-08-26 13:12

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_admin', '0039_alter_aboutpage_page_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='page_banner',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='page_content',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='page_title',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='secendary_title',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='page_banner',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='page_content',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='page_title',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='secendary_title',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='new_arrival1_button_link',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='new_arrival1_button_text',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='new_arrival1_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='new_arrival1_image',
            field=models.ImageField(blank=True, default='blank-landscape.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='new_arrival1_secondary_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='new_arrival2_button_link',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='new_arrival2_button_text',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='new_arrival2_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='new_arrival2_image',
            field=models.ImageField(blank=True, default='blank-landscape.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='new_arrival2_secondary_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slide1_button_link',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slide1_button_text',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slide1_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slide1_image',
            field=models.ImageField(blank=True, default='blank-landscape.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slide1_secondary_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slide2_button_link',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slide2_button_text',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slide2_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slide2_image',
            field=models.ImageField(blank=True, default='blank-landscape.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slide2_secondary_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='special_offer_banner1_button_text',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='special_offer_banner1_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='special_offer_banner1_image',
            field=models.ImageField(blank=True, default='blank-landscape.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='special_offer_banner1_secondary_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='special_offer_banner2_button_text',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='special_offer_banner2_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='special_offer_banner2_image',
            field=models.ImageField(blank=True, default='blank-landscape.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='special_offer_banner2_secondary_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='special_offer_banner3_button_text',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='special_offer_banner3_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='special_offer_banner3_image',
            field=models.ImageField(blank=True, default='blank-landscape.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='special_offer_banner3_secondary_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='special_offer_button_link1',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='special_offer_button_link2',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='special_offer_button_link3',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='tranding_banner',
            field=models.ImageField(blank=True, default='blank-landscape.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='tranding_button_link',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='tranding_button_text',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='tranding_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='tranding_secondary_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='trust_box1_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='trust_box1_icon',
            field=models.ImageField(blank=True, default='blank-landscape.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='trust_box1_secondary_text',
            field=models.CharField(blank=True, default='', max_length=600),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='trust_box2_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='trust_box2_icon',
            field=models.ImageField(blank=True, default='blank-landscape.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='trust_box2_secondary_text',
            field=models.CharField(blank=True, default='', max_length=600),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='trust_box3_heading',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='trust_box3_icon',
            field=models.ImageField(blank=True, default='blank-landscape.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='trust_box3_secondary_text',
            field=models.CharField(blank=True, default='', max_length=600),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True),
        ),
    ]
