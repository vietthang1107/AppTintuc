# Generated by Django 3.2.9 on 2021-12-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='author',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
