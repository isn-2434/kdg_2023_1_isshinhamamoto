# Generated by Django 4.2.7 on 2024-01-23 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycle', '0003_cycle_brake_rate_cycle_frame_rate_cycle_gire_rate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cycle',
            old_name='bike',
            new_name='bike_thumnail',
        ),
    ]