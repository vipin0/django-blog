# Generated by Django 2.2.6 on 2019-10-29 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_topic_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(max_length=6000),
        ),
    ]
