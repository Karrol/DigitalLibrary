# Generated by Django 2.2.5 on 2019-12-25 12:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='person_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sex', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=4, verbose_name='性别')),
                ('name', models.CharField(max_length=30, verbose_name='用户姓名')),
                ('Password', models.CharField(max_length=30, verbose_name='密码')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='无分组数字图书馆系统用户')),
            ],
        ),
        migrations.CreateModel(
            name='readerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(max_length=13, verbose_name='读者类型名')),
                ('bookNum', models.CharField(max_length=3, verbose_name='读者类型可借书籍')),
            ],
        ),
        migrations.CreateModel(
            name='librarian_info',
            fields=[
                ('person_info_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='login.person_info')),
                ('gonghao', models.CharField(max_length=13, unique=True, verbose_name='馆员工号')),
                ('photo', models.ImageField(blank=True, upload_to='media/zhangli/librarian', verbose_name='头像')),
            ],
            bases=('login.person_info',),
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('person_info_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='login.person_info')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('max_borrowing', models.IntegerField(default=15, verbose_name='可借数量')),
                ('balance', models.FloatField(default=0.0, verbose_name='余额')),
                ('photo', models.ImageField(blank=True, upload_to='readerimg', verbose_name='头像')),
                ('inTime', models.DateField(default='2019-12-19', verbose_name='登记日期')),
                ('birth_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='创建时间')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='住址')),
                ('phone', models.CharField(blank=True, max_length=11, verbose_name='联系电话')),
                ('occupation', models.CharField(blank=True, choices=[(1, '经理'), (2, '专业技术'), (3, '技师技工'), (4, '社区和个人服务'), (5, '文秘行政'), (6, '销售'), (7, '机械操作和驾驶类'), (8, '体力劳动类')], max_length=255, verbose_name='职业')),
                ('status', models.IntegerField(choices=[(0, 'normal'), (-1, 'overdue')], default=0)),
            ],
            options={
                'verbose_name': '读者',
                'verbose_name_plural': '读者',
                'ordering': ['inTime'],
            },
            bases=('login.person_info',),
        ),
    ]
