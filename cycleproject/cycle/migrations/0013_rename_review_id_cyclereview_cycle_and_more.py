# Generated by Django 4.2.7 on 2024-01-28 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycle', '0012_rename_review_cyclereview_wheelreview_framereview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cyclereview',
            old_name='review_id',
            new_name='cycle',
        ),
        migrations.RenameField(
            model_name='framereview',
            old_name='review_id',
            new_name='frame',
        ),
        migrations.RenameField(
            model_name='wheelreview',
            old_name='review_id',
            new_name='wheel',
        ),
    ]
