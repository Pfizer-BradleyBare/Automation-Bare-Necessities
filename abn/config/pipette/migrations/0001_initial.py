# Generated by Django 4.1.6 on 2024-07-23 20:54

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiquidClass',
            fields=[
                ('liquid_class_name', models.CharField(help_text='Liquid class name as defined in the Hamilton liquid class editor.', max_length=50, primary_key=True, serialize=False, unique=True)),
                ('min_volume', models.FloatField()),
                ('max_volume', models.FloatField()),
            ],
            options={
                'ordering': ['liquid_class_name'],
            },
        ),
        migrations.CreateModel(
            name='LiquidClassCategory',
            fields=[
                ('identifier', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('category', models.CharField(choices=[('Viscosity:Low; Volatility:Low; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:Low; Volatility:Low; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:Low; Volatility:Low; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Low; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:Low; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:High; Volatility:High; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:High; Volatility:High; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:High; Volatility:High; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:High; Volatility:High; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:High; Volatility:High; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:High; Volatility:High; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:High; Volatility:High; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:High; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar')], max_length=81)),
            ],
            options={
                'ordering': ['identifier'],
            },
        ),
        migrations.CreateModel(
            name='PipetteBase',
            fields=[
                ('identifier', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('enabled', models.BooleanField(default=True)),
                ('waste_labware_id', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['identifier'],
            },
        ),
        migrations.CreateModel(
            name='HamiltonPortraitCORE8',
            fields=[
                ('pipettebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pipette.pipettebase')),
                ('active_channels', multiselectfield.db.fields.MultiSelectField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16')], max_length=38)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('pipette.pipettebase',),
        ),
        migrations.CreateModel(
            name='PipetteTip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip_support_dropoff_labware_id', models.CharField(max_length=100)),
                ('tip_support_pickup_labware_id', models.CharField(max_length=100)),
                ('supported_aspirate_liquid_class_categories', models.ManyToManyField(related_name='+', to='pipette.liquidclasscategory')),
                ('supported_dispense_liquid_class_categories', models.ManyToManyField(related_name='+', to='pipette.liquidclasscategory')),
            ],
            options={
                'ordering': ['tip'],
            },
        ),
    ]
