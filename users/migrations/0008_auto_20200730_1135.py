# Generated by Django 3.0.6 on 2020-07-30 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200715_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('email', 'email'), ('Github', 'Github'), ('Kakao', 'Kakao')], default='email', max_length=50),
        ),
    ]