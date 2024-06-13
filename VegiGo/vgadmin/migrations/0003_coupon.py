# Generated by Django 5.0.3 on 2024-05-01 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vgadmin', '0002_alter_branches_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('discount', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('minimum_purchase', models.IntegerField()),
            ],
        ),
    ]