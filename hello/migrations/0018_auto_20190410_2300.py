# Generated by Django 2.1.1 on 2019-04-10 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0017_auto_20190410_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardetail',
            name='card',
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.DeleteModel(
            name='CarDetail',
        ),
    ]
