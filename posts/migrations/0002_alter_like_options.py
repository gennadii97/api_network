# Generated by Django 4.2.3 on 2023-07-29 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ['created_time']},
        ),
    ]
