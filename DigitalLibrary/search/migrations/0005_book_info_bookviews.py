# Generated by Django 2.2.5 on 2019-12-17 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20191213_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_info',
            name='bookViews',
            field=models.PositiveIntegerField(default=0),
        ),
    ]