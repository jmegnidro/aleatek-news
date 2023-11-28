# Generated by Django 3.2.19 on 2023-06-19 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mission', '0005_alter_mission_mission_parent'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashbord', '0026_auto_20230618_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvisArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codification', models.CharField(choices=[('F', 'F'), ('RMQ', 'RMQ'), ('HM', 'HM'), ('SO', 'SO'), ('IM', 'IM')], max_length=5)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mission.article')),
                ('collaborateurs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RICT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('statut', models.CharField(choices=[(0, 'En cours'), (1, 'Accepté'), (2, 'Classé'), (3, 'Diffuse')], default=0, max_length=10)),
                ('affaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashbord.affaire')),
            ],
        ),
        migrations.CreateModel(
            name='Disposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('commentaire', models.CharField(max_length=300)),
                ('rict', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RICT.rict')),
            ],
        ),
        migrations.CreateModel(
            name='CommentaireAvisArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.CharField(max_length=200)),
                ('a_suivre', models.BooleanField(default=True)),
                ('id_avis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RICT.avisarticle')),
            ],
        ),
    ]
