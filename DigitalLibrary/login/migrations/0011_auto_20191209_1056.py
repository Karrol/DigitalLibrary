# Generated by Django 2.2.5 on 2019-12-09 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20191209_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='phone',
            field=models.IntegerField(blank=True, verbose_name='电话'),
        ),
    ]
