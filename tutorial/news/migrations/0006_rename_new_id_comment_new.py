# Generated by Django 3.2.9 on 2021-12-21 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20211221_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='new_id',
            new_name='new',
        ),
    ]
