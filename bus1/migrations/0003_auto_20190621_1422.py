# Generated by Django 2.2.2 on 2019-06-21 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus1', '0002_auto_20190621_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_ID',
            field=models.IntegerField(default=1234),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_ids',
            field=models.IntegerField(default='6389'),
        ),
    ]
