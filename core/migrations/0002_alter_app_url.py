# Generated by Django 4.2.3 on 2023-07-30 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='url',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
