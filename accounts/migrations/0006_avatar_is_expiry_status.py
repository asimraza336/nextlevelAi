# Generated by Django 3.2 on 2023-07-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20230727_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='is_expiry_status',
            field=models.BooleanField(default=True),
        ),
    ]
