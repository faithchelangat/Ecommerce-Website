# Generated by Django 4.2.14 on 2024-08-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_order_alter_shippingaddress_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(default=False),
        ),
    ]
