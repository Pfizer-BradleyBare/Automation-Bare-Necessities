# Generated by Django 4.1.6 on 2024-07-15 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('heat_cool_shake', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
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
