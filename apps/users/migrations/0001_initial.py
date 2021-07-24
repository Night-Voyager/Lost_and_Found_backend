# Generated by Django 2.1 on 2020-02-28 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('studentID', models.PositiveIntegerField(default='')),
                ('openID', models.CharField(default='', max_length=50)),
                ('unionID', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
