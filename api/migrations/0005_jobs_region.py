# Generated by Django 2.2.3 on 2019-08-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190802_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='region',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]