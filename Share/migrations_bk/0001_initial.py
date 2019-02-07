# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('DownloadDocount', models.IntegerField(verbose_name='下载次数', default=0)),
                ('code', models.CharField(verbose_name='code', max_length=10)),
                ('Datatime', models.DateTimeField(default=datetime.datetime.now)),
                ('path', models.CharField(verbose_name='下载路径', max_length=32)),
                ('name', models.CharField(verbose_name='文件名', max_length=32, default='')),
                ('Filesize', models.CharField(verbose_name='文件大小', max_length=10)),
                ('PCIP', models.CharField(verbose_name='IP地址', max_length=32, default='')),
                ('bikou', models.CharField(verbose_name='文件description', max_length=100)),
            ],
            options={
                'verbose_name': 'download1',
                'db_table': 'download1',
                'verbose_name_plural': 'download1',
            },
        ),
    ]
