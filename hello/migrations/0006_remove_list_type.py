# Generated by Django 2.1.1 on 2019-02-18 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='type',
        ),
    ]
