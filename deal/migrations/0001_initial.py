# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-03 06:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BOSStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(choices=[(0, '买'), (1, '卖')], default=0, verbose_name='买卖角色')),
                ('amount', models.IntegerField(verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='挂单时间')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.Stock', verbose_name='股票')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '挂单表',
                'verbose_name_plural': '挂单表',
            },
        ),
        migrations.CreateModel(
            name='DealList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(max_length=20, verbose_name='交易记录号')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='交易时间')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='成交价格')),
                ('amount', models.IntegerField(verbose_name='数量')),
                ('stock', models.CharField(max_length=20, verbose_name='股票')),
                ('buser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buser', to=settings.AUTH_USER_MODEL, verbose_name='买家')),
                ('suser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suser', to=settings.AUTH_USER_MODEL, verbose_name='卖家')),
            ],
            options={
                'verbose_name': '交易记录表',
                'verbose_name_plural': '交易记录表',
            },
        ),
        migrations.CreateModel(
            name='SelfStcok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.Stock', verbose_name='股票')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '交易表',
                'verbose_name_plural': '交易表',
            },
        ),
    ]
