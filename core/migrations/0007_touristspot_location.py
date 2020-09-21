# Generated by Django 3.1.1 on 2020-09-21 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('core', '0006_touristspot_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='locations.location'),
            preserve_default=False,
        ),
    ]