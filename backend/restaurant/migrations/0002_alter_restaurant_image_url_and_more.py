# Generated by Django 4.0.4 on 2022-04-27 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image_url',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='image_url',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]