# Generated by Django 2.1.2 on 2019-05-15 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20190511_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='visiting',
            field=models.PositiveIntegerField(default=0, verbose_name='浏览数'),
        ),
    ]