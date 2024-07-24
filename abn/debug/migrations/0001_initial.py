# Generated by Django 4.1.6 on 2024-07-24 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TraceEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('log_source', models.CharField(choices=[('PLH', 'PLH'), ('ABN', 'ABN')], max_length=3)),
                ('log_level', models.CharField(choices=[('DEBUG', 'DEBUG'), ('INFO', 'INFO'), ('WARNING', 'WARNING'), ('CRITICAL', 'CRITICAL'), ('ERROR', 'ERROR')], max_length=10)),
                ('device_identifier', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.queuedmethod')),
            ],
            options={
                'ordering': ['time_stamp'],
            },
        ),
    ]