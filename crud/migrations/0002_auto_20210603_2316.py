# Generated by Django 3.2.4 on 2021-06-03 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='email',
            field=models.EmailField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
