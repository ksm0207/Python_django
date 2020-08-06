# Generated by Django 3.0.6 on 2020-08-06 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200730_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, verbose_name='bio'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('영어', '영어'), ('한국어', '한국어'), ('중국어', '중국어'), ('일본어', '일본어')], default='한국어', max_length=25, verbose_name='language'),
        ),
    ]
