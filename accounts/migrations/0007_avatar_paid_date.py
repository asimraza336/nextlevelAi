# Generated by Django 3.2 on 2023-07-27 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_avatar_is_expiry_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='paid_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
