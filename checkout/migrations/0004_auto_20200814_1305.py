# Generated by Django 3.1 on 2020-08-14 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_orderlineitem_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='booking_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_required',
            field=models.BooleanField(default=False),
        ),
    ]
