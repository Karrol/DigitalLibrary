# Generated by Django 2.2.5 on 2019-12-26 12:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('search', '0001_initial'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='readerSearchlist_sculib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_date', models.DateTimeField(blank=True, default=None, null=True, verbose_name='查询时间')),
                ('ISBN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.book_shumu', verbose_name='ISBN')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Reader', verbose_name='读者')),
            ],
            options={
                'verbose_name': '我的查询历史',
                'verbose_name_plural': '我的查询历史',
            },
        ),
        migrations.CreateModel(
            name='readerSearchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_date', models.DateTimeField(blank=True, default=None, null=True, verbose_name='查询时间')),
                ('ISBN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.book_info', verbose_name='ISBN')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Reader', verbose_name='读者')),
            ],
            options={
                'verbose_name': '我的查询历史',
                'verbose_name_plural': '我的查询历史',
            },
        ),
        migrations.CreateModel(
            name='readerLibrary_sculib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('In_date', models.DateField(default=django.utils.timezone.now, verbose_name='加入时间')),
                ('defBookType', models.CharField(default='我的图书分区', max_length=200, verbose_name='加入时间')),
                ('ISBN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.book_shumu', verbose_name='ISBN')),
                ('reader', models.ForeignKey(default='51', on_delete=django.db.models.deletion.CASCADE, to='login.Reader', verbose_name='读者')),
            ],
            options={
                'verbose_name': '我的图书馆',
                'verbose_name_plural': '我的图书馆',
            },
        ),
        migrations.CreateModel(
            name='readerLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('In_date', models.DateField(default=django.utils.timezone.now, verbose_name='加入时间')),
                ('defBookType', models.CharField(default='我的图书分区', max_length=200, verbose_name='加入时间')),
                ('ISBN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.book_info', verbose_name='ISBN')),
                ('reader', models.ForeignKey(default='51', on_delete=django.db.models.deletion.CASCADE, to='login.Reader', verbose_name='读者')),
            ],
            options={
                'verbose_name': '我的图书馆',
                'verbose_name_plural': '我的图书馆',
            },
        ),
        migrations.CreateModel(
            name='moneyTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(blank='False', max_length=256, verbose_name='事务名称')),
                ('price', models.CharField(blank='False', max_length=1000, verbose_name='事务花费')),
                ('inTime', models.DateField(verbose_name='事务发生日期')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Reader', verbose_name='读者')),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing_sculib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateField(verbose_name='借出时间')),
                ('date_due_to_returned', models.DateField(verbose_name='应还时间')),
                ('date_returned', models.DateField(null=True, verbose_name='还书时间')),
                ('amount_of_fine', models.FloatField(default=0.0, verbose_name='欠款')),
                ('ISBN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.book_shumu', verbose_name='ISBN')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Reader', verbose_name='读者')),
            ],
            options={
                'verbose_name': '借阅',
                'verbose_name_plural': '借阅',
            },
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateField(verbose_name='借出时间')),
                ('date_due_to_returned', models.DateField(verbose_name='应还时间')),
                ('date_returned', models.DateField(null=True, verbose_name='还书时间')),
                ('amount_of_fine', models.FloatField(default=0.0, verbose_name='欠款')),
                ('ISBN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.book_info', verbose_name='ISBN')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Reader', verbose_name='读者')),
            ],
            options={
                'verbose_name': '借阅',
                'verbose_name_plural': '借阅',
            },
        ),
        migrations.CreateModel(
            name='adviceforSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank='False', max_length=256, verbose_name='建议主题')),
                ('advice', models.CharField(blank='False', max_length=1000, verbose_name='读者对系统的建议')),
                ('inTime', models.DateField(verbose_name='建议日期')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Reader', verbose_name='读者')),
            ],
        ),
    ]
