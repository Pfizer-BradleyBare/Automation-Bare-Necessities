# Generated by Django 4.1.6 on 2024-07-25 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('centrifuge', '0001_initial'),
        ('layout_item', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='centrifugebase',
            name='plates',
            field=models.ManyToManyField(to='layout_item.layoutitembase'),
        ),
        migrations.AddField(
            model_name='centrifugebase',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
    ]
