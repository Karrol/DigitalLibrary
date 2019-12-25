# Generated by Django 2.2.5 on 2019-12-25 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('search', '0001_initial'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='person_info',
            fields=[
                ('Sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('Name', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('Password', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='reader_info',
            fields=[
                ('person_info_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='librarian.person_info')),
                ('telNumber', models.CharField(blank=True, max_length=20, verbose_name='电话')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('readertypeName', models.CharField(blank=True, max_length=30, verbose_name='读者类型名称')),
                ('bookNumber', models.IntegerField(verbose_name='书籍上限')),
            ],
            bases=('librarian.person_info',),
        ),
        migrations.CreateModel(
            name='bookborrow_info',
            fields=[
                ('brID', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='图书借阅事务ID')),
                ('borrowTime', models.DateTimeField(verbose_name='借阅时间')),
                ('expirationTime', models.DateTimeField(verbose_name='应归还时间')),
                ('ifBack', models.BooleanField(default=False, verbose_name='是否归还')),
                ('ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.Reader')),
                ('bookID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='search.book_info')),
                ('librarian', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='librarian_info_bookborrow', to='login.librarian_info')),
            ],
        ),
        migrations.CreateModel(
            name='bookback_info',
            fields=[
                ('bcID', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='图书归还事务ID')),
                ('backTime', models.DateTimeField(verbose_name='借阅时间')),
                ('ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.Reader')),
                ('bookID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='search.book_info')),
                ('librarian', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='librarian_info_bookback', to='login.librarian_info')),
            ],
        ),
    ]
