# Generated by Django 3.1 on 2020-08-14 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_remove_order_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=6),
        ),
    ]
