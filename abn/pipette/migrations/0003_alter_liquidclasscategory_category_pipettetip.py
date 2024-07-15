# Generated by Django 4.1.6 on 2024-07-15 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tip', '0001_initial'),
        ('pipette', '0002_remove_liquidclass_num_labware_positions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquidclasscategory',
            name='category',
            field=models.CharField(choices=[('Viscosity:Low; Volatility:Low; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:Low; Volatility:Low; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:Low; Volatility:Low; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Low; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:Low; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:Low; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:Low; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:Low; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:Low; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:Medium; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:Medium; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:Medium; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:Medium; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:High; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:High; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:High; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Homogenous; Polarity:Non_Polar', 'Viscosity:High; Volatility:High; Homogeneity:Homogenous; Polarity:Non-Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Homogenous; Polarity:Polar', 'Viscosity:High; Volatility:High; Homogeneity:Homogenous; Polarity:Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Emulsion; Polarity:Non_Polar', 'Viscosity:High; Volatility:High; Homogeneity:Emulsion; Polarity:Non-Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Emulsion; Polarity:Polar', 'Viscosity:High; Volatility:High; Homogeneity:Emulsion; Polarity:Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Suspension; Polarity:Non_Polar', 'Viscosity:High; Volatility:High; Homogeneity:Suspension; Polarity:Non-Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Suspension; Polarity:Polar', 'Viscosity:High; Volatility:High; Homogeneity:Suspension; Polarity:Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Heterogenous; Polarity:Non_Polar', 'Viscosity:High; Volatility:High; Homogeneity:Heterogenous; Polarity:Non-Polar'), ('Viscosity:High; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar', 'Viscosity:High; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar')], max_length=81),
        ),
        migrations.CreateModel(
            name='PipetteTip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip_support_dropoff_labware_id', models.CharField(max_length=100)),
                ('tip_support_pickup_labware_id', models.CharField(max_length=100)),
                ('supported_aspirate_liquid_class_categories', models.ManyToManyField(related_name='+', to='pipette.liquidclasscategory')),
                ('supported_dispense_liquid_class_categories', models.ManyToManyField(related_name='+', to='pipette.liquidclasscategory')),
                ('tip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tip.tipbase')),
            ],
            options={
                'ordering': ['tip'],
            },
        ),
    ]
