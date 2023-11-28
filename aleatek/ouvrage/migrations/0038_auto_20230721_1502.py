# Generated by Django 3.2.12 on 2023-07-21 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashbord', '0027_auto_20230621_0044'),
        ('ouvrage', '0037_remarqueaso_aso'),
    ]

    operations = [
        migrations.AddField(
            model_name='affaireouvrage',
            name='rename',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='ouvrage',
            name='affaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dashbord.affaire'),
        ),
    ]
