# Generated by Django 2.2.5 on 2019-12-17 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readerCenter', '0003_auto_20191217_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readerlibrary',
            name='In_date',
            field=models.DateField(verbose_name='加入时间'),
        ),
        migrations.AlterField(
            model_name='readerlibrary',
            name='defBookType',
            field=models.CharField(max_length=200, verbose_name='加入时间'),
        ),
    ]
