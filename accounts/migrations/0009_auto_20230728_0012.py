# Generated by Django 3.2 on 2023-07-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20230727_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='gmail',
            field=models.EmailField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='avatar',
            name='password',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
