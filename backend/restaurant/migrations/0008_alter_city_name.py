# Generated by Django 4.0.4 on 2022-04-29 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_city_image_alter_city_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
