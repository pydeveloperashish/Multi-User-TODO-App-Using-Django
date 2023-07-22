# Generated by Django 4.2.3 on 2023-07-22 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_todo_priority_todo_status_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('C', 'COMPLETED'), ('P', 'PENDING')], default='', max_length=2),
        ),
    ]
