# Generated by Django 3.0.6 on 2020-06-15 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20200615_0944'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='rooms',
            field=models.ManyToManyField(blank=True, related_name='lists', to='rooms.Room'),
        ),
        migrations.AlterField(
            model_name='list',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to=settings.AUTH_USER_MODEL),
        ),
    ]
