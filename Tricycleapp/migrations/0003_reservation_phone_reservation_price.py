# Generated by Django 4.2.5 on 2023-09-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tricycleapp', '0002_remove_reservation_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='phone',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='reservation',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
