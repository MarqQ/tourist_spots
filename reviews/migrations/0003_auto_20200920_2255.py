# Generated by Django 3.1.1 on 2020-09-21 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20200920_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
