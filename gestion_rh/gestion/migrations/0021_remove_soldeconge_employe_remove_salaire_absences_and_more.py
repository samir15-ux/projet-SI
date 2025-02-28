# Generated by Django 5.1.3 on 2025-01-17 03:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0020_salaire_avance_alter_conge_employe_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soldeconge',
            name='employe',
        ),
        migrations.RemoveField(
            model_name='salaire',
            name='absences',
        ),
        migrations.RemoveField(
            model_name='salaire',
            name='avance',
        ),
        migrations.RemoveField(
            model_name='salaire',
            name='mois',
        ),
        migrations.RemoveField(
            model_name='salaire',
            name='salaire_final',
        ),
        migrations.AddField(
            model_name='salaire',
            name='heures_supplementaires',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='salaire',
            name='employe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Conges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_conge', models.CharField(choices=[('annuel', 'Congé Annuel'), ('maladie', 'Congé Maladie'), ('maternite', 'Congé Maternité/Paternité'), ('sans_solde', 'Congé Sans Solde')], max_length=20)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('statut', models.BooleanField(default=False)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Conge',
        ),
        migrations.DeleteModel(
            name='SoldeConge',
        ),
    ]
