# Generated by Django 3.2.19 on 2023-06-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0006_articleselect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='titre',
            field=models.CharField(max_length=500),
        ),
    ]
