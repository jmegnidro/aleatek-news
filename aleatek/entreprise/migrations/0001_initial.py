# Generated by Django 4.2 on 2023-05-31 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adresse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raison_sociale', models.CharField(max_length=100)),
                ('siret', models.IntegerField()),
                ('activite', models.CharField(max_length=200)),
                ('adresse', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='adresse.adress')),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Responsables', to='entreprise.entreprise')),
            ],
        ),
    ]