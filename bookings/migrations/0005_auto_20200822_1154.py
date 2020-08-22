# Generated by Django 3.1 on 2020-08-22 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_remove_booking_booking_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
