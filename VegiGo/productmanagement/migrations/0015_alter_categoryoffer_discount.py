# Generated by Django 5.0.3 on 2024-05-01 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0014_alter_product_unit_type_categoryoffer_productoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryoffer',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]