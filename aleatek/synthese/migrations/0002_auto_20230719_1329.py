# Generated by Django 3.2.12 on 2023-07-19 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synthese', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='syntheseavis',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='syntheseavis',
            name='statut',
            field=models.CharField(choices=[(0, 'En cours'), (1, 'Accepté'), (2, 'Classé'), (3, 'Diffuse')], default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='syntheseavis',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]