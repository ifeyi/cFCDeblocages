# Generated by Django 5.1.6 on 2025-02-27 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evenement_suivant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('libele', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Type_alerte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('libele', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Type_de_pret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=100)),
                ('libele', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Type_evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('libele', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('datedebut', models.CharField(max_length=100)),
                ('datefin', models.CharField(max_length=100)),
                ('libele', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('evenementsuivant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfcdeblocagesmiseenplace.evenement_suivant')),
                ('typeevenement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfcdeblocagesmiseenplace.type_evenement')),
            ],
        ),
        migrations.CreateModel(
            name='Alerte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('declencheur', models.CharField(max_length=100)),
                ('libele', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('evenement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfcdeblocagesmiseenplace.evenement')),
                ('typealerte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfcdeblocagesmiseenplace.type_alerte')),
            ],
        ),
        migrations.CreateModel(
            name='Dossier_de_pret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('unitcode', models.CharField(max_length=100)),
                ('clientcode', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=255)),
                ('productcode', models.CharField(max_length=100)),
                ('reference', models.CharField(max_length=100)),
                ('capitalnominal', models.CharField(max_length=100)),
                ('maxterm', models.CharField(max_length=100)),
                ('externalrib', models.CharField(max_length=100)),
                ('externalribbankcode', models.CharField(max_length=100)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('rib', models.CharField(max_length=100)),
                ('bankcode', models.CharField(max_length=100)),
                ('udate', models.DateField()),
                ('cdate', models.DateField()),
                ('franchiseduration', models.CharField(max_length=100)),
                ('agreementdate', models.DateField()),
                ('datefirstallotement', models.DateField()),
                ('echpremi', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('statusdate', models.DateField()),
                ('evenement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfcdeblocagesmiseenplace.evenement')),
                ('typedepret', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfcdeblocagesmiseenplace.type_de_pret')),
            ],
        ),
        migrations.CreateModel(
            name='Conditions_primo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=100)),
                ('libele', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('typedepret', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfcdeblocagesmiseenplace.type_de_pret')),
            ],
        ),
    ]
