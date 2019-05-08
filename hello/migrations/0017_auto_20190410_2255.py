# Generated by Django 2.1.1 on 2019-04-10 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0016_auto_20190410_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(default='', max_length=30, verbose_name='卡号')),
                ('card_user', models.CharField(default='', max_length=10, verbose_name='姓名')),
                ('add_time', models.DateField(auto_now=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '银行卡账户',
                'verbose_name': '银行卡账户_基本信息',
            },
        ),
        migrations.CreateModel(
            name='CarDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(default='', max_length=30, verbose_name='电话')),
                ('mail', models.CharField(default='', max_length=30, verbose_name='邮箱')),
                ('city', models.CharField(default='', max_length=10, verbose_name='城市')),
                ('address', models.CharField(default='', max_length=30, verbose_name='详细地址')),
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hello.Card', verbose_name='卡号')),
            ],
            options={
                'verbose_name_plural': '个人资料',
                'verbose_name': '账户_个人资料',
            },
        ),
        migrations.DeleteModel(
            name='Uboxall',
        ),
    ]
