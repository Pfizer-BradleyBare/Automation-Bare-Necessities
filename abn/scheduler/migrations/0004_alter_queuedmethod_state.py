# Generated by Django 4.1.6 on 2024-07-29 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_queuedmethod_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queuedmethod',
            name='state',
            field=models.CharField(choices=[('Complete', 'Complete'), ('Aborted', 'Aborted'), ('Notification', 'Notification'), ('Running', 'Running'), ('Paused', 'Paused'), ('Not Running', 'Not Running'), ('Paused', 'Paused'), ('Deck Loading', 'Deck Loading')], default='Not Running', max_length=12),
        ),
    ]