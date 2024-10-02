# Generated by Django 5.1.1 on 2024-10-02 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('block', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('method', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockbase',
            name='method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='method.usermethodbase'),
        ),
        migrations.AddField(
            model_name='blockbase',
            name='middle_child',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='block.blockbase'),
        ),
        migrations.AddField(
            model_name='blockbase',
            name='middle_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='block.blockbase'),
        ),
        migrations.AddField(
            model_name='blockbase',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='blockbase',
            name='right_child',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='block.blockbase'),
        ),
        migrations.AddField(
            model_name='blockbase',
            name='right_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='block.blockbase'),
        ),
    ]
