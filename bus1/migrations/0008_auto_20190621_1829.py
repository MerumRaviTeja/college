# Generated by Django 2.2.2 on 2019-06-21 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus1', '0007_auto_20190621_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(default='0539'),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(max_length=4),
        ),
    ]