# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_remove_album_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='release_year',
            field=models.IntegerField(default=2015),
            preserve_default=False,
        ),
    ]
