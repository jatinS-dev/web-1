# Generated by Django 2.2.4 on 2020-10-12 03:26

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0153_hackathonevent_use_circle'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='override_dict',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Used to admin override anything in the dic representation of this profile'),
        ),
    ]
