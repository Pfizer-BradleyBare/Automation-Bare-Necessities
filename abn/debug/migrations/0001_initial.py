# Generated by Django 4.1.6 on 2024-08-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TraceEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('log_source', models.IntegerField(choices=[(1, 'Plh'), (2, 'Abn')])),
                ('log_level', models.IntegerField(choices=[(1, 'Debug'), (2, 'Info'), (3, 'Warning'), (4, 'Critical'), (5, 'Error')])),
                ('device_identifier', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'ordering': ['time_stamp'],
            },
        ),
    ]
