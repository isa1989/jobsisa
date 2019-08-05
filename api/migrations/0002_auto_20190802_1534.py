# Generated by Django 2.2.3 on 2019-08-02 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='sosialid',
        ),
        migrations.AddField(
            model_name='sosiallink',
            name='jobsid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sosialid', to='api.Jobs'),
            preserve_default=False,
        ),
    ]