# Generated by Django 4.2.3 on 2023-07-22 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('1', '1️⃣'), ('2', '2️⃣'), ('3', '3️⃣'), ('4', '4️⃣'), ('5', '5️⃣'), ('6', '6️⃣'), ('7', '7️⃣'), ('8', '8️⃣'), ('9', '9️⃣'), ('10', '🔟')], default='', max_length=2),
        ),
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('C', 'COMPLETED'), ('F', 'PENDING')], default='', max_length=2),
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
