# Generated by Django 5.0.6 on 2024-07-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_delete_syatemsetting_restaurant_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemsetting',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
