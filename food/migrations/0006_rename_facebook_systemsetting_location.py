# Generated by Django 5.0.6 on 2024-07-05 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_systemsetting_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='systemsetting',
            old_name='facebook',
            new_name='location',
        ),
    ]
