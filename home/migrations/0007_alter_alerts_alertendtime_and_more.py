# Generated by Django 4.2.11 on 2024-04-17 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_alerts_motionid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts',
            name='alertEndTime',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='alerts',
            name='alertStartTime',
            field=models.CharField(max_length=8),
        ),
    ]
