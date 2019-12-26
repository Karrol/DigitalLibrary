# Generated by Django 2.2.6 on 2019-12-26 03:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('participate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recbooklistinfo',
            name='RecName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recbooklistinfo',
            name='bpubTime',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]