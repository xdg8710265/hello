# Generated by Django 2.1.1 on 2019-04-03 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_auto_20190318_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bank',
            options={'verbose_name_plural': 'ubox-银行卡'},
        ),
        migrations.AlterModelOptions(
            name='cardinfo',
            options={'verbose_name_plural': 'ubox-卡号信息'},
        ),
    ]