# Generated by Django 5.1.2 on 2024-10-11 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0004_rename_meta_data_text_author_value_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='value',
            new_name='meta_data_text',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='value',
            new_name='meta_data_text',
        ),
        migrations.RenameField(
            model_name='documentnumber',
            old_name='value',
            new_name='meta_data_text',
        ),
        migrations.RenameField(
            model_name='modality',
            old_name='value',
            new_name='meta_data_text',
        ),
        migrations.RenameField(
            model_name='pipette',
            old_name='volume',
            new_name='volume_ul',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='value',
            new_name='meta_data_text',
        ),
    ]