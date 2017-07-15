# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0007_users'),
        ('goods_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('goods', models.ForeignKey(to='goods_info.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMain',
            fields=[
                ('order_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('state', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to='user_info.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(to='order_info.OrderMain'),
        ),
    ]
