# Generated by Django 3.0.6 on 2021-12-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.TextField()),
                ('author', models.TextField()),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
