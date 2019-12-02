# Generated by Django 2.2.5 on 2019-11-29 01:38

from django.db import migrations, models
import django.db.models.deletion
import search.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book_info',
            fields=[
                ('ISBN', models.CharField(max_length=13, primary_key=True, serialize=False, verbose_name='ISBN')),
                ('title', models.CharField(max_length=128, verbose_name='书名')),
                ('author', models.CharField(max_length=32, verbose_name='作者')),
                ('press', models.CharField(max_length=64, verbose_name='出版社')),
                ('description', models.CharField(default='', max_length=1024, verbose_name='书籍简介')),
                ('category', models.CharField(default='文学', max_length=64, verbose_name='分类')),
                ('cover', models.ImageField(blank=True, default='null', upload_to=search.models.custom_path, verbose_name='封面')),
                ('index', models.CharField(max_length=16, null=True, verbose_name='索引')),
                ('bookTranslator', models.CharField(blank=True, max_length=30, verbose_name='译者')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='书籍价格')),
                ('page', models.IntegerField(blank=True, verbose_name='图书页码')),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
            },
        ),
        migrations.CreateModel(
            name='bookshelf_info',
            fields=[
                ('bookshelfID', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='书架财产编号')),
                ('bookshelfName', models.CharField(default='文学I21', max_length=50, verbose_name='书架名称')),
            ],
        ),
        migrations.CreateModel(
            name='bookEntity_info',
            fields=[
                ('bookID', models.IntegerField(primary_key=True, serialize=False, verbose_name='图书财产ID')),
                ('location', models.CharField(default='图书馆1楼', max_length=64, verbose_name='位置')),
                ('quantity', models.IntegerField(default=1, verbose_name='数量')),
                ('booksearchID', models.CharField(max_length=10, unique=True, verbose_name='索书号')),
                ('bookIntime', models.DateTimeField(verbose_name='图书入库时间')),
                ('bookshelfid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.bookshelf_info')),
            ],
        ),
    ]
