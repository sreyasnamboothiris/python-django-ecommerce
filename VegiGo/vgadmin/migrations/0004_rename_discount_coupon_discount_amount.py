# Generated by Django 5.0.3 on 2024-05-03 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vgadmin', '0003_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='discount',
            new_name='discount_amount',
        ),
    ]