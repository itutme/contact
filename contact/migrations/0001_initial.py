# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('company', models.CharField(max_length=30, blank=True)),
                ('phone_mobile', models.CharField(max_length=30)),
                ('phone_work', models.CharField(max_length=30, blank=True)),
                ('phone_home', models.CharField(max_length=30, blank=True)),
                ('profile_photo', models.ImageField(upload_to=b'photo/%Y/%m', blank=True)),
                ('address', models.TextField(blank=True)),
                ('city', models.CharField(max_length=30, blank=True)),
                ('state', models.CharField(max_length=15, blank=True)),
                ('country', models.CharField(max_length=2, blank=True)),
                ('postal_zip', models.CharField(max_length=10, blank=True)),
                ('email', models.CharField(max_length=100, blank=True)),
                ('website', models.CharField(max_length=100, blank=True)),
                ('note', models.TextField(blank=True)),
                ('ip', models.TextField(help_text='e.g. Skype: johndoe', verbose_name='Instant Messenger', blank=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
