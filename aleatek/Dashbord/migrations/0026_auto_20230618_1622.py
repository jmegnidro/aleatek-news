# Generated by Django 3.2.19 on 2023-06-18 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashbord', '0025_alter_chantier_batiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affaire',
            name='assistant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DashbordAffaireassistant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='affaire',
            name='charge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DashbordAffairecharge', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='affaire',
            name='chef',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DashbordAffairechef', to=settings.AUTH_USER_MODEL),
        ),
    ]