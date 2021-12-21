# Generated by Django 3.2.9 on 2021-12-21 07:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20211221_0810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'ordering': ['date_created']},
        ),
        migrations.RenameField(
            model_name='new',
            old_name='dayCreate',
            new_name='date_created',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_cmt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('content', models.TextField(blank=True, default='', null=True)),
                ('user_cmt', models.TextField(blank=True, default='', null=True)),
                ('new_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.new', verbose_name='Id of new')),
            ],
        ),
    ]
