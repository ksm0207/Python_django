# Generated by Django 3.0.6 on 2020-07-06 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_auto_20200616_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.IntegerField(help_text='예약문의 010-9600-5982'),
        ),
    ]
