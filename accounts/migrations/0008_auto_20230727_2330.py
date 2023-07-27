# Generated by Django 3.2 on 2023-07-27 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_avatar_paid_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='is_expiry_status',
        ),
        migrations.AddField(
            model_name='avatar',
            name='is_not_expired',
            field=models.BooleanField(default=False),
        ),
    ]