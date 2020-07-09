# Generated by Django 3.0.6 on 2020-07-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200706_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('email', 'Email'), ('Github', 'Github'), ('Kakao', 'Kakao')], default='email', max_length=50),
        ),
    ]