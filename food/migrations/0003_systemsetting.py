# Generated by Django 5.0.6 on 2024-07-03 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_booktable'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=250)),
                ('slogan', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('logo', models.ImageField(upload_to='sys')),
                ('facebook', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
