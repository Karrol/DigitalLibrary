# Generated by Django 2.2.5 on 2019-12-09 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_auto_20191209_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person_info',
            name='role',
        ),
    ]
