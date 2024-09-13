# Generated by Django 4.1.6 on 2024-08-07 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('method', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executingmethod',
            name='state',
            field=models.CharField(choices=[('Reading', 'Reading'), ('Running', 'Running'), ('Paused', 'Paused'), ('Waiting on User', 'Waiting on User'), ('Complete', 'Complete'), ('Aborted', 'Aborted'), ('Cleanup', 'Cleanup')], default='Reading', max_length=15),
        ),
    ]