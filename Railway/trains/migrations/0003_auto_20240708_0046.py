# Generated by Django 3.1.7 on 2024-07-07 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0002_auto_20240707_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='balance',
            field=models.IntegerField(default=1000),
        ),
    ]
