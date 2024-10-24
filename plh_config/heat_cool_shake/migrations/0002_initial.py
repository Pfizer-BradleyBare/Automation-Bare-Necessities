# Generated by Django 5.1.1 on 2024-10-09 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('heat_cool_shake', '0001_initial'),
        ('layout_item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='heatcoolshakebase',
            name='plates',
            field=models.ManyToManyField(to='layout_item.layoutitembase'),
        ),
        migrations.AddField(
            model_name='heatcoolshakebase',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
    ]
