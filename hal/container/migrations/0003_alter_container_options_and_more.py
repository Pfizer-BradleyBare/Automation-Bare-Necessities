# Generated by Django 5.1.2 on 2024-11-11 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("container", "0002_alter_container_identifier"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="container",
            options={"ordering": ["name"]},
        ),
        migrations.RenameField(
            model_name="container",
            old_name="identifier",
            new_name="name",
        ),
    ]
