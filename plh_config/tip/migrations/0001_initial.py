# Generated by Django 5.1.1 on 2024-10-03 21:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('layout_item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipBase',
            fields=[
                ('identifier', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('enabled', models.BooleanField(default=True)),
                ('tip_volume', models.FloatField()),
                ('backend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.backendbase')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
                ('tip_racks', models.ManyToManyField(to='layout_item.layoutitembase')),
            ],
            options={
                'ordering': ['identifier'],
            },
        ),
        migrations.CreateModel(
            name='HamiltonEETipBase',
            fields=[
                ('tipbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tip.tipbase')),
                ('tip_rack_waste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layout_item.layoutitembase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('tip.tipbase',),
        ),
        migrations.CreateModel(
            name='HamiltonFTR',
            fields=[
                ('tipbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tip.tipbase')),
            ],
            options={
                'verbose_name': 'Hamilton FTR',
                'verbose_name_plural': 'Hamilton FTRs',
            },
            bases=('tip.tipbase',),
        ),
        migrations.CreateModel(
            name='HamiltonEETipStack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_number', models.PositiveSmallIntegerField()),
                ('stack_number', models.PositiveSmallIntegerField()),
                ('tip_rack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layout_item.layoutitembase')),
            ],
            options={
                'verbose_name': 'Hamilton EE tip stack',
                'verbose_name_plural': 'Hamilton EE tip stacks',
            },
        ),
        migrations.CreateModel(
            name='HamiltonEEFTR1000uL',
            fields=[
                ('hamiltoneetipbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tip.hamiltoneetipbase')),
            ],
            options={
                'verbose_name': 'Hamilton EE FTR 1000uL',
                'verbose_name_plural': 'Hamilton EE FTR 1000uLs',
            },
            bases=('tip.hamiltoneetipbase',),
        ),
        migrations.CreateModel(
            name='HamiltonEENTR',
            fields=[
                ('hamiltoneetipbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tip.hamiltoneetipbase')),
            ],
            options={
                'verbose_name': 'Hamilton EE NTR',
                'verbose_name_plural': 'Hamilton EE NTRs',
            },
            bases=('tip.hamiltoneetipbase',),
        ),
        migrations.AddField(
            model_name='hamiltoneetipbase',
            name='tip_stacks',
            field=models.ManyToManyField(to='tip.hamiltoneetipstack'),
        ),
        migrations.CreateModel(
            name='HamiltonNTR',
            fields=[
                ('tipbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tip.tipbase')),
                ('tip_rack_waste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layout_item.layoutitembase')),
            ],
            options={
                'verbose_name': 'Hamilton NTR',
                'verbose_name_plural': 'Hamilton NTRs',
            },
            bases=('tip.tipbase',),
        ),
    ]
