# Generated by Django 4.2.14 on 2024-08-13 09:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShippingAdress',
            new_name='ShippingAddress',
        ),
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name_plural': 'ShippingAddress'},
        ),
    ]
