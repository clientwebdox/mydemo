# Generated by Django 4.0.4 on 2022-05-31 05:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 5, 35, 46, 292217, tzinfo=utc)),
        ),
    ]