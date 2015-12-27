# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GBook',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('pierwsze_imie', models.CharField(max_length=8)),
                ('drugie_imie', models.CharField(max_length=8)),
                ('nazwisko', models.CharField(max_length=12)),
                ('zawód', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=10)),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'guestbook',
            },
        ),
    ]
