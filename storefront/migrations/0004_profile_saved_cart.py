# Generated by Django 4.2.14 on 2024-08-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='saved_cart',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
