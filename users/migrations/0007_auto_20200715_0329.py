# Generated by Django 3.0.6 on 2020-07-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_login_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=True),
        ),
    ]
