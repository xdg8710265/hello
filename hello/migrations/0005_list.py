# Generated by Django 2.1.1 on 2019-02-18 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.CharField(max_length=100)),
                ('type', models.IntegerField(max_length=10)),
            ],
        ),
    ]
