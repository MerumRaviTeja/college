# Generated by Django 2.2.2 on 2019-06-21 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus1', '0005_auto_20190621_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_ID',
            new_name='stude',
        ),
        migrations.AlterField(
            model_name='student',
            name='stud',
            field=models.IntegerField(default='9509'),
        ),
    ]
