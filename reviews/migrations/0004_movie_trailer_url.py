# Generated by Django 3.2.13 on 2022-11-05 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20221103_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer_url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]