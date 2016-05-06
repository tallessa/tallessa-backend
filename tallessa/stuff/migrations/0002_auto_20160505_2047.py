# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 17:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tallessa_teams', '0001_initial'),
        ('tallessa_stuff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='tallessa_teams.Team'),
        ),
        migrations.AddField(
            model_name='item',
            name='current_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallessa_stuff.Place'),
        ),
        migrations.AddField(
            model_name='item',
            name='home_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='as_current_place_for_items', to='tallessa_stuff.Place'),
        ),
        migrations.AddField(
            model_name='item',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='tallessa_stuff.Item'),
        ),
        migrations.AddField(
            model_name='item',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stuff', to='tallessa_teams.Team'),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('team', 'slug')]),
        ),
        migrations.AlterIndexTogether(
            name='item',
            index_together=set([('team', 'serial_number')]),
        ),
    ]
