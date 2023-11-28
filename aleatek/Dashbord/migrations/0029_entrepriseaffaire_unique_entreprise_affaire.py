# Generated by Django 3.2.12 on 2023-07-25 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashbord', '0028_remove_entrepriseaffaire_unique_entreprise_affaire'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='entrepriseaffaire',
            constraint=models.UniqueConstraint(fields=('entreprise', 'affaire'), name='unique_entreprise_affaire'),
        ),
    ]