# Generated by Django 3.2.7 on 2021-09-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject_id', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=64)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]