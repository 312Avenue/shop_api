# Generated by Django 4.0.5 on 2022-07-21 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_price_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Цена'),
        ),
    ]
