# Generated by Django 2.1.1 on 2018-11-23 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_test_up_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='up_date',
        ),
    ]
