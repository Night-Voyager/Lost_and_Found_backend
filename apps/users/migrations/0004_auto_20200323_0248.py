# Generated by Django 2.1 on 2020-03-23 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200228_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='openID',
        ),
        migrations.RemoveField(
            model_name='student',
            name='unionID',
        ),
    ]
