# Generated by Django 5.1.2 on 2024-10-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("block", "0005_rename_value_author_meta_data_text_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="incubateandshake",
            name="shaking_rpm",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="incubateandshake",
            name="temperature",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="incubateandshake",
            name="time",
            field=models.FloatField(null=True),
        ),
    ]