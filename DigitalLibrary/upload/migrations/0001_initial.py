# Generated by Django 2.2.6 on 2019-12-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wenjian', models.CharField(max_length=20)),
                ('lujing', models.CharField(max_length=60)),
                ('uname', models.CharField(max_length=14)),
                ('isActive', models.BooleanField(default=True)),
                ('shareduser', models.CharField(max_length=14)),
            ],
        ),
    ]