# Generated by Django 2.1.1 on 2019-02-26 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('auth', models.CharField(max_length=10)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('up_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='cus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('psw', models.CharField(max_length=40)),
                ('mail', models.CharField(max_length=50)),
            ],
        ),
    ]
