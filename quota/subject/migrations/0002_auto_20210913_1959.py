# Generated by Django 3.2.7 on 2021-09-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='semester',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='subject',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='year',
            field=models.IntegerField(default=None),
        ),
    ]
