# Generated by Django 3.1.2 on 2020-12-19 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='place',
            field=models.CharField(default='unknown', max_length=100),
        ),
    ]
