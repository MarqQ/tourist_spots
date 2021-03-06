# Generated by Django 3.1.1 on 2020-09-21 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('core', '0007_touristspot_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='touristic_spot'),
        ),
        migrations.AlterField(
            model_name='touristspot',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.location'),
        ),
    ]
