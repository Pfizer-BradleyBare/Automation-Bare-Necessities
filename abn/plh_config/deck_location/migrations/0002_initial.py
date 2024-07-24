# Generated by Django 4.1.6 on 2024-07-24 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transport', '0001_initial'),
        ('deck_location', '0001_initial'),
        ('carrier', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportconfig',
            name='get_options',
            field=models.ManyToManyField(to='transport.transportgetoptions'),
        ),
        migrations.AddField(
            model_name='transportconfig',
            name='place_options',
            field=models.ManyToManyField(to='transport.transportplaceoptions'),
        ),
        migrations.AddField(
            model_name='transportconfig',
            name='transport_device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.transportbase'),
        ),
        migrations.AddField(
            model_name='decklocationbase',
            name='carrier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrier.carrierbase'),
        ),
        migrations.AddField(
            model_name='decklocationbase',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='transportabledecklocation',
            name='transport_configs',
            field=models.ManyToManyField(to='deck_location.transportconfig'),
        ),
    ]
