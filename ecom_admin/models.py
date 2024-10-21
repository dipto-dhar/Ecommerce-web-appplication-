
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
import datetime
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from django.core.exceptions import ValidationError
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    first_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, blank=True, default='')
    description = models.CharField(max_length=255, blank=True, default='')
    image = models.ImageField(blank=True, default='profile.png',null=True)
    phone = models.IntegerField(null=True)
    groups=models.ForeignKey(Group,on_delete=models.CASCADE,default='4',null=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.first_name + self.last_name
    
    def get_short_name(self):
        return self.first_name or self.email.split('@')[0]
class Category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(default='blank-landscape.jpg',null=True)
    description=models.CharField(max_length=50)
    slug=AutoSlugField(populate_from=('name'),unique=True,null=True)
    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + self.last_name
    
class Product(models.Model):
    name=models.CharField(max_length=500,default='')
    sku=models.CharField(max_length=100,)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description=HTMLField(default='',blank=True)
    regular_price= models.DecimalField(max_digits=7,default=0,decimal_places=2)
    sale_price= models.DecimalField(max_digits=7,default=0, blank=True, null=True, decimal_places=2)
    on_sale=models.BooleanField(default=False)
    image=models.ImageField(upload_to='uploads/products', default='blank-sm.png', null=True)
    stock=models.BooleanField(default=True)
    date=models.DateField(default=datetime.datetime.now)
    slug = AutoSlugField(populate_from=('name'),unique=True,null=True, )
    is_featured=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class ShippingZone(models.Model):
    name= models.CharField(max_length=50, default='', null=True, blank=True)
    country= models.CharField(max_length=50, default='', null=True, blank=True)
    state= models.CharField(max_length=50, default='', null=True, blank=True)
    city= models.CharField(max_length=50, default='', null=True, blank=True)
    method=models.CharField(max_length=50)
    cost=models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True ,null=True)
    free_limit=models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Shipping Zone"
    
    

    




class Homepage(models.Model):
    # Main Slider
    slider=models.BooleanField(default=True)
    # Slide 1
    slide1_image= models.ImageField(blank=True, default='blank-landscape.jpg',)
    slide1_heading= models.CharField(max_length=500, blank=True, default='' )
    slide1_secondary_heading= models.CharField(max_length=500, blank=True, default='' )
    slide1_button_text= models.CharField(max_length=500, blank=True, default='' )
    slide1_button_link= models.CharField(max_length=1000, blank=True, default='')
    # Slide 1
    slide2_image= models.ImageField(blank=True, default='blank-landscape.jpg',)
    slide2_heading= models.CharField(max_length=500, blank=True, default='' )
    slide2_secondary_heading= models.CharField(max_length=500, blank=True, default='' )
    slide2_button_text= models.CharField(max_length=500, blank=True, default='' )
    slide2_button_link= models.CharField(max_length=1000, blank=True, default='')
    # Special Offer Section
    special_offer_banner=models.BooleanField(default=True)
    # Banner 1
    special_offer_banner1_image= models.ImageField(blank=True, default='blank-landscape.jpg',)
    special_offer_banner1_heading= models.CharField(max_length=500, blank=True, default='' )
    special_offer_banner1_secondary_heading= models.CharField(max_length=500, blank=True, default='' )
    special_offer_banner1_button_text= models.CharField(max_length=500, blank=True, default='' )
   
    special_offer_button_link1= models.CharField(max_length=1000, blank=True, default='' )
    # Banner 2
    special_offer_banner2_image= models.ImageField(blank=True, default='blank-landscape.jpg',)
    special_offer_banner2_heading= models.CharField(max_length=500, blank=True, default='' )
    special_offer_banner2_secondary_heading= models.CharField(max_length=500, blank=True, default='' )
    special_offer_banner2_button_text= models.CharField(max_length=500, blank=True, default='' )
    special_offer_button_link2= models.CharField(max_length=1000, blank=True, default='' )
    # Banner 3
    special_offer_banner3_image= models.ImageField(blank=True, default='blank-landscape.jpg',)
    special_offer_banner3_heading= models.CharField(max_length=500, blank=True, default='' )
    special_offer_banner3_secondary_heading= models.CharField(max_length=500, blank=True, default='' )
    special_offer_banner3_button_text= models.CharField(max_length=500, blank=True, default='' )
    special_offer_button_link3= models.CharField(max_length=1000, blank=True, default='' )
    # Trending Section
    tranding_section=models.BooleanField(default=True)
    tranding_banner=models.ImageField(blank=True, default='blank-landscape.jpg',)
    tranding_heading= models.CharField(max_length=500, blank=True, default='' )
    tranding_secondary_heading= models.CharField(max_length=500, blank=True, default='' )
    tranding_button_text= models.CharField(max_length=500, blank=True, default='' )
    tranding_button_link= models.CharField(max_length=1000, blank=True, default='' )
    
    # New Arrival Section
    new_arrival=models.BooleanField(default=True)
    # Banner 1
    new_arrival1_image= models.ImageField(blank=True, default='blank-landscape.jpg',)
    new_arrival1_heading= models.CharField(max_length=500, blank=True, default='' )
    new_arrival1_secondary_heading= models.CharField(max_length=500, blank=True, default='' )
    new_arrival1_button_text= models.CharField(max_length=500, blank=True, default='' )
    new_arrival1_button_link= models.CharField(max_length=1000, blank=True, default='')
    # Banner 1
    new_arrival2_image= models.ImageField(blank=True, default='blank-landscape.jpg',)
    new_arrival2_heading= models.CharField(max_length=500, blank=True, default='' )
    new_arrival2_secondary_heading= models.CharField(max_length=500, blank=True, default='', )
    new_arrival2_button_text= models.CharField(max_length=500, blank=True, default='', )
    new_arrival2_button_link= models.CharField(max_length=1000, blank=True, default='')

    # Trust & Support Section
    trust_box=models.BooleanField(default=True)
    # Box 1
    trust_box1_icon=models.ImageField(blank=True, default='blank-landscape.jpg',)
    trust_box1_heading= models.CharField(max_length=500, blank=True, default='' )
    trust_box1_secondary_text= models.CharField(max_length=600, blank=True, default='' )
    # Box 2
    trust_box2_icon=models.ImageField(blank=True, default='blank-landscape.jpg',)
    trust_box2_heading= models.CharField(max_length=500, blank=True, default='' )
    trust_box2_secondary_text= models.CharField(max_length=600, blank=True, default='' )
    # Box 3
    trust_box3_icon=models.ImageField(blank=True, default='blank-landscape.jpg',)
    trust_box3_heading= models.CharField(max_length=500, blank=True, default='' )
    trust_box3_secondary_text= models.CharField(max_length=600, blank=True, default='' )

 
class AboutPage(models.Model):
    page_title= models.CharField(max_length=500,blank=True, default='' )
    secendary_title= models.CharField(max_length=500,blank=True, default='' )
    page_banner=models.ImageField(blank=True, default='', null=True)
    page_content=HTMLField(default='',blank=True, )

class ContactPage(models.Model):
    page_title= models.CharField(max_length=500,blank=True, default='' )
    secendary_title= models.CharField(max_length=500,blank=True, default='' )
    page_banner=models.ImageField(blank=True, default='', null=True)
    page_content=HTMLField(default='',blank=True, )

class TermsPage(models.Model):
    page_title= models.CharField(max_length=500,blank=True, default='' )
    secendary_title= models.CharField(max_length=500,blank=True, default='' )
    page_banner=models.ImageField(blank=True, default='', null=True)
    page_content=HTMLField(default='',blank=True, )
    
class PrivacyPolicyPage(models.Model):
    page_title= models.CharField(max_length=500,blank=True, default='' )
    secendary_title= models.CharField(max_length=500,blank=True, default='' )
    page_banner=models.ImageField(blank=True, default='', null=True)
    page_content=HTMLField(default='',blank=True, )


class Settings(models.Model):
    SITE_CURRENCIES = [
    ('$', 'USD - United States Dollar ($)'),
    ('€', 'EUR - Euro (€)'),
    ('£', 'GBP - British Pound Sterling (£)'),
    ('¥', 'JPY - Japanese Yen (¥)'),
    ('A$', 'AUD - Australian Dollar (A$)'),
    ('C$', 'CAD - Canadian Dollar (C$)'),
    ('CHF', 'CHF - Swiss Franc (CHF)'),
    ('¥', 'CNY - Chinese Yuan (¥)'),
    ('HK$', 'HKD - Hong Kong Dollar (HK$)'),
    ('NZ$', 'NZD - New Zealand Dollar (NZ$)'),
    ('kr', 'SEK - Swedish Krona (kr)'),
    ('₩', 'KRW - South Korean Won (₩)'),
    ('S$', 'SGD - Singapore Dollar (S$)'),
    ('kr', 'NOK - Norwegian Krone (kr)'),
    ('$', 'MXN - Mexican Peso ($)'),
    ('₹', 'INR - Indian Rupee (₹)'),
    ('₽', 'RUB - Russian Ruble (₽)'),
    ('R', 'ZAR - South African Rand (R)'),
    ('₺', 'TRY - Turkish Lira (₺)'),
    ('R$', 'BRL - Brazilian Real (R$)'),
    ('NT$', 'TWD - New Taiwan Dollar (NT$)'),
    ('kr', 'DKK - Danish Krone (kr)'),
    ('zł', 'PLN - Polish Złoty (zł)'),
    ('฿', 'THB - Thai Baht (฿)'),
    ('Rp', 'IDR - Indonesian Rupiah (Rp)'),
    ('Ft', 'HUF - Hungarian Forint (Ft)'),
    ('Kč', 'CZK - Czech Koruna (Kč)'),
    ('₪', 'ILS - Israeli New Shekel (₪)'),
    ('$', 'CLP - Chilean Peso ($)'),
    ('₱', 'PHP - Philippine Peso (₱)'),
    ('د.إ', 'AED - United Arab Emirates Dirham (د.إ)'),
    ('$', 'COP - Colombian Peso ($)'),
    ('﷼', 'SAR - Saudi Riyal (﷼)'),
    ('RM', 'MYR - Malaysian Ringgit (RM)'),
    ('lei', 'RON - Romanian Leu (lei)'),

    ('$', 'ARS - Argentine Peso ($)'),
    ('֏', 'AMD - Armenian Dram (֏)'),
    ('₼', 'AZN - Azerbaijani Manat (₼)'),
    ('৳', 'BDT - Bangladeshi Taka (৳)'),
    ('$', 'BSD - Bahamian Dollar ($)'),
    ('$', 'BBD - Barbadian Dollar ($)'),
    ('Br', 'BYN - Belarusian Ruble (Br)'),
    ('$', 'BZD - Belize Dollar ($)'),
    ('₣', 'BIF - Burundian Franc (₣)'),
    ('$', 'BMD - Bermudian Dollar ($)'),
    ('$', 'BND - Brunei Dollar ($)'),
    ('$', 'BOV - Bolivian Mvdol ($)'),
    ('$', 'BOB - Bolivian Boliviano ($)'),
    ('KM', 'BAM - Bosnia and Herzegovina Convertible Mark (KM)'),
    ('P', 'BWP - Botswana Pula (P)'),
    ('₣', 'BIF - Burundian Franc (₣)'),
    ('$', 'KYD - Cayman Islands Dollar ($)'),
    ('FC', 'CDF - Congolese Franc (FC)'),
    ('$', 'FJD - Fijian Dollar ($)'),
    ('L', 'HNL - Honduran Lempira (L)'),
    ('$', 'TTD - Trinidad and Tobago Dollar ($)'),
    ('$', 'XCD - East Caribbean Dollar ($)'),
    ('$', 'GIP - Gibraltar Pound (£)'),
    ('₣', 'GNF - Guinean Franc (₣)'),
    ('Q', 'GTQ - Guatemalan Quetzal (Q)'),
    ('$', 'GYD - Guyanese Dollar ($)'),
    ('$', 'JMD - Jamaican Dollar ($)'),
    ('L', 'HNL - Honduran Lempira (L)'),
    ('$', 'XCD - East Caribbean Dollar ($)'),
    ('$', 'SBD - Solomon Islands Dollar ($)'),
    ('$', 'TOP - Tongan Paʻanga (T$)'),
    ('$', 'BND - Brunei Dollar ($)'),
    ('₼', 'TMT - Turkmenistani Manat (₼)'),
    ('Sh', 'TZS - Tanzanian Shilling (Sh)'),
    ('UGX', 'UGX - Ugandan Shilling (UGX)'),
    ('₴', 'UAH - Ukrainian Hryvnia (₴)'),
    ('Sh', 'KES - Kenyan Shilling (Sh)'),
    ('$', 'VUV - Vanuatu Vatu (VUV)'),
    ('₫', 'VND - Vietnamese đồng (₫)'),
    ('Kz', 'AOA - Angolan Kwanza (Kz)'),
    ('Fr', 'XAF - CFA Franc BEAC (Fr)'),
    ('₣', 'XPF - CFP Franc (₣)'),
    ('$', 'LRD - Liberian Dollar ($)'),
    ('₣', 'XOF - CFA Franc BCEAO (₣)'),
    ('$', 'SLL - Sierra Leonean Leone ($)')

]
    SITE_COUNTRIES = [
    ('AFG', 'Afghanistan'),
    ('ALB', 'Albania'),
    ('DZA', 'Algeria'),
    ('AND', 'Andorra'),
    ('AGO', 'Angola'),
    ('ATG', 'Antigua and Barbuda'),
    ('ARG', 'Argentina'),
    ('ARM', 'Armenia'),
    ('AUS', 'Australia'),
    ('AUT', 'Austria'),
    ('AZE', 'Azerbaijan'),
    ('BHS', 'Bahamas'),
    ('BHR', 'Bahrain'),
    ('BGD', 'Bangladesh'),
    ('BRB', 'Barbados'),
    ('BLR', 'Belarus'),
    ('BEL', 'Belgium'),
    ('BLZ', 'Belize'),
    ('BEN', 'Benin'),
    ('BTN', 'Bhutan'),
    ('BOL', 'Bolivia'),
    ('BIH', 'Bosnia and Herzegovina'),
    ('BWA', 'Botswana'),
    ('BRA', 'Brazil'),
    ('BRN', 'Brunei Darussalam'),
    ('BGR', 'Bulgaria'),
    ('BFA', 'Burkina Faso'),
    ('BDI', 'Burundi'),
    ('KHM', 'Cambodia'),
    ('CMR', 'Cameroon'),
    ('CAN', 'Canada'),
    ('CPV', 'Cape Verde'),
    ('CAF', 'Central African Republic'),
    ('TCD', 'Chad'),
    ('CHL', 'Chile'),
    ('CHN', 'China'),
    ('COL', 'Colombia'),
    ('COM', 'Comoros'),
    ('COG', 'Congo'),
    ('CRI', 'Costa Rica'),
    ('CIV', "Côte d'Ivoire"),
    ('HRV', 'Croatia'),
    ('CUB', 'Cuba'),
    ('CYP', 'Cyprus'),
    ('CZE', 'Czech Republic'),
    ('DNK', 'Denmark'),
    ('DJI', 'Djibouti'),
    ('DMA', 'Dominica'),
    ('DOM', 'Dominican Republic'),
    ('ECU', 'Ecuador'),
    ('EGY', 'Egypt'),
    ('SLV', 'El Salvador'),
    ('GNQ', 'Equatorial Guinea'),
    ('ERI', 'Eritrea'),
    ('EST', 'Estonia'),
    ('SWZ', 'Eswatini'),
    ('ETH', 'Ethiopia'),
    ('FJI', 'Fiji'),
    ('FIN', 'Finland'),
    ('FRA', 'France'),
    ('GAB', 'Gabon'),
    ('GMB', 'Gambia'),
    ('GEO', 'Georgia'),
    ('DEU', 'Germany'),
    ('GHA', 'Ghana'),
    ('GRC', 'Greece'),
    ('GRD', 'Grenada'),
    ('GTM', 'Guatemala'),
    ('GIN', 'Guinea'),
    ('GNB', 'Guinea-Bissau'),
    ('GUY', 'Guyana'),
    ('HTI', 'Haiti'),
    ('HND', 'Honduras'),
    ('HUN', 'Hungary'),
    ('ISL', 'Iceland'),
    ('IND', 'India'),
    ('IDN', 'Indonesia'),
    ('IRN', 'Iran'),
    ('IRQ', 'Iraq'),
    ('IRL', 'Ireland'),
    ('ISR', 'Israel'),
    ('ITA', 'Italy'),
    ('JAM', 'Jamaica'),
    ('JPN', 'Japan'),
    ('JOR', 'Jordan'),
    ('KAZ', 'Kazakhstan'),
    ('KEN', 'Kenya'),
    ('KIR', 'Kiribati'),
    ('KWT', 'Kuwait'),
    ('KGZ', 'Kyrgyzstan'),
    ('LAO', "Lao People's Democratic Republic"),
    ('LVA', 'Latvia'),
    ('LBN', 'Lebanon'),
    ('LSO', 'Lesotho'),
    ('LBR', 'Liberia'),
    ('LBY', 'Libya'),
    ('LIE', 'Liechtenstein'),
    ('LTU', 'Lithuania'),
    ('LUX', 'Luxembourg'),
    ('MDG', 'Madagascar'),
    ('MWI', 'Malawi'),
    ('MYS', 'Malaysia'),
    ('MDV', 'Maldives'),
    ('MLI', 'Mali'),
    ('MLT', 'Malta'),
    ('MHL', 'Marshall Islands'),
    ('MRT', 'Mauritania'),
    ('MUS', 'Mauritius'),
    ('MEX', 'Mexico'),
    ('FSM', 'Micronesia'),
    ('MDA', 'Moldova'),
    ('MCO', 'Monaco'),
    ('MNG', 'Mongolia'),
    ('MNE', 'Montenegro'),
    ('MAR', 'Morocco'),
    ('MOZ', 'Mozambique'),
    ('MMR', 'Myanmar'),
    ('NAM', 'Namibia'),
    ('NRU', 'Nauru'),
    ('NPL', 'Nepal'),
    ('NLD', 'Netherlands'),
    ('NZL', 'New Zealand'),
    ('NIC', 'Nicaragua'),
    ('NER', 'Niger'),
    ('NGA', 'Nigeria'),
    ('MKD', 'North Macedonia'),
    ('NOR', 'Norway'),
    ('OMN', 'Oman'),
    ('PAK', 'Pakistan'),
    ('PLW', 'Palau'),
    ('PAN', 'Panama'),
    ('PNG', 'Papua New Guinea'),
    ('PRY', 'Paraguay'),
    ('PER', 'Peru'),
    ('PHL', 'Philippines'),
    ('POL', 'Poland'),
    ('PRT', 'Portugal'),
    ('QAT', 'Qatar'),
    ('ROU', 'Romania'),
    ('RUS', 'Russian Federation'),
    ('RWA', 'Rwanda'),
    ('KNA', 'Saint Kitts and Nevis'),
    ('LCA', 'Saint Lucia'),
    ('VCT', 'Saint Vincent and the Grenadines'),
    ('WSM', 'Samoa'),
    ('SMR', 'San Marino'),
    ('STP', 'Sao Tome and Principe'),
    ('SAU', 'Saudi Arabia'),
    ('SEN', 'Senegal'),
    ('SRB', 'Serbia'),
    ('SYC', 'Seychelles'),
    ('SLE', 'Sierra Leone'),
    ('SGP', 'Singapore'),
    ('SVK', 'Slovakia'),
    ('SVN', 'Slovenia'),
    ('SLB', 'Solomon Islands'),
    ('SOM', 'Somalia'),
    ('ZAF', 'South Africa'),
    ('SSD', 'South Sudan'),
    ('ESP', 'Spain'),
    ('LKA', 'Sri Lanka'),
    ('SDN', 'Sudan'),
    ('SUR', 'Suriname'),
    ('SWE', 'Sweden'),
    ('CHE', 'Switzerland'),
    ('SYR', 'Syrian Arab Republic'),
    ('TWN', 'Taiwan'),
    ('TJK', 'Tajikistan'),
    ('TZA', 'Tanzania'),
    ('THA', 'Thailand'),
    ('TLS', 'Timor-Leste'),
    ('TGO', 'Togo'),
    ('TON', 'Tonga'),
    ('TTO', 'Trinidad and Tobago'),
    ('TUN', 'Tunisia'),
    ('TUR', 'Turkey'),
    ('TKM', 'Turkmenistan'),
    ('TUV', 'Tuvalu'),
    ('UGA', 'Uganda'),
    ('UKR', 'Ukraine'),
    ('ARE', 'United Arab Emirates'),
    ('GBR', 'United Kingdom'),
    ('USA', 'United States of America'),
    ('URY', 'Uruguay'),
    ('UZB', 'Uzbekistan'),
    ('VUT', 'Vanuatu'),
    ('VEN', 'Venezuela'),
    ('VNM', 'Viet Nam'),
    ('YEM', 'Yemen'),
    ('ZMB', 'Zambia'),
    ('ZWE', 'Zimbabwe'),
    # Add more countries as needed
    ]
    site_name = models.CharField(max_length=255)
    site_tagline = models.CharField(max_length=255)
    site_description = models.TextField(blank=True)
    store_address = models.TextField(blank=True)
    primary_color=models.CharField(max_length=10, default='',blank=True)
    button_color=models.CharField(max_length=10, default='',blank=True)
    button_bg_color=models.CharField(max_length=10, default='',blank=True)
    heading_color=models.CharField(max_length=10, default='',blank=True)
    contact_email = models.EmailField(blank=True)
    admin_email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20,blank=True)
    store_country = models.CharField(max_length=3, choices=SITE_COUNTRIES, default='USA')
    store_currency = models.CharField(max_length=3, choices=SITE_CURRENCIES, default='USD')
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    favicon = models.ImageField(upload_to='favicons/', blank=True, null=True)
    fb_link=models.CharField(max_length=240,default='',blank=True)
    insta_link=models.CharField(max_length=240,default='',blank=True)
    twiter_link=models.CharField(max_length=240,default='',blank=True)
    linkedin_link=models.CharField(max_length=240,default='',blank=True)
    pinterest_link=models.CharField(max_length=240,default='',blank=True)
    copyright = models.CharField(max_length=255, default='',blank=True)
    meta_title = models.CharField(max_length=255,blank=True)
    meta_description = models.TextField(blank=True)
    additional_css = models.TextField(max_length=5000,default='',null=True,blank=True)

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return "Site Settings"

    def clean(self):
        if Settings.objects.exists() and not self.pk:
            raise ValidationError('There can be only one Settings instance')

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Settings, self).save(*args, **kwargs)