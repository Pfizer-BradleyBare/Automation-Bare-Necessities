# Generated by Django 4.1.6 on 2024-07-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_alter_queuedmethod_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queuedmethod',
            name='state',
            field=models.CharField(choices=[('Deck Loading', 'Deck Loading'), ('Notification', 'Notification'), ('In Queue', 'In Queue'), ('Running', 'Running'), ('Paused', 'Paused'), ('Complete', 'Complete'), ('Aborted', 'Aborted')], default='Not Running', max_length=12),
        ),
    ]