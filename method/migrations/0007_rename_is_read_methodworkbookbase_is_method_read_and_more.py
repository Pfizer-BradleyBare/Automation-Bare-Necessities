# Generated by Django 5.1.2 on 2024-10-30 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("method", "0006_rename_is_full_read_methodworkbookbase_is_read_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="methodworkbookbase",
            old_name="is_read",
            new_name="is_method_read",
        ),
        migrations.AddField(
            model_name="methodworkbookbase",
            name="is_solutions_read",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="methodworkbookbase",
            name="is_worklist_read",
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
