# Generated by Django 5.1.2 on 2024-10-23 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("method", "0003_methodworkbookbase_is_full_read"),
    ]

    operations = [
        migrations.AddField(
            model_name="testingmethodworkbook",
            name="test_progress",
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
